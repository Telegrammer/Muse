from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget, QDialog, QTableWidget

from src.DialogFormFactory import DialogFormFactory
from src.Emitters import VoidEmitter, TupleEmitter
from .ManagerMainWindowView import ManagerMainWindowView
from .gantaDiagram import Ui_Form
from typing import Callable

__all__ = ["ManagerMainWindow"]


class ManagerMainWindow(QMainWindow, ManagerMainWindowView):

    def __init__(self, parent_signal: VoidEmitter):
        QWidget.__init__(self, None)
        self.setupUi(self)

        self.__quit_session_signal = parent_signal
        self.quitSessionAction.triggered.connect(
            lambda: self.__quit_session_signal.signal.emit()
        )

        self.addExhibitionButton.clicked.connect(
            lambda: self.form_dialog("Добавить выставку", "Добавить", "Выставка",
                                     operation=self.add_exhibition, table=self.exhibitionTable)
        )

        self.openExhibitionCalendarButton.clicked.connect(self.open_calendar)

    @staticmethod
    def __focus_change(focused_widgets: list[QWidget], unfocused_widgets: list[QWidget]):
        for widget in focused_widgets:
            widget.setEnabled(True)
        for widget in unfocused_widgets:
            widget.setEnabled(False)

    @staticmethod
    def __get_row_data(table_widget: QTableWidget) -> list[tuple[str]]:
        selected_row: int = table_widget.currentRow()
        column_count: int = table_widget.columnCount()
        result: list[tuple[str]] = []
        for i in range(column_count):
            try:
                result.append((table_widget.horizontalHeaderItem(i).text(),
                               table_widget.item(selected_row, i).text())
                              )
            except AttributeError:
                result.append((table_widget.horizontalHeaderItem(i).text(),
                               ""
                               ))
        return result

    def form_dialog(self, window_title: str, button_label: str, table_name: str,
                    operation: Callable, table: QTableWidget):
        dialog_factory: DialogFormFactory = DialogFormFactory(window_title, button_label, table_name,
                                                              self.__get_row_data(table))
        send_data_signal = TupleEmitter(self)
        send_data_signal.signal.connect(operation)
        dialog_form: QDialog = dialog_factory(send_data_signal)
        dialog_form.show()
        dialog_form.exec_()

    def add_exhibition(self, dialog_output: tuple[str]):
        print(dialog_output, print(self.exhibitionTable.columnCount() == len(dialog_output)))

    def open_calendar(self):
        Form = QDialog(None)
        Form.setModal(True)
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        Form.exec_()
