from typing import Callable

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget, QDialog, QAction, QTableWidgetItem

from src.Emitters import VoidEmitter, TupleEmitter
from src.SharedWidgets.MuseDialog.DialogFormFactory import DialogFormFactory
from .ManagerMainWindowView import ManagerMainWindowView
from .gantaDiagram import Ui_Form
from ..SharedWidgets.MuseTableWidget import MuseTableWidget
from ..SharedWidgets.MuseDialog import MuseDialogWidget

__all__ = ["ManagerMainWindow"]


class ManagerMainWindow(QMainWindow, ManagerMainWindowView):

    def __init__(self, parent_signal: VoidEmitter):
        QWidget.__init__(self, None)
        self.setupUi(self)

        self.setVisibleExhibitionTableButton.clicked.connect(
            lambda: self.__set_visible_table(self.managerExhibitionTableWidget, self.selectExhibitionTableAction)
        )
        self.selectExhibitionTableAction.changed.connect(
            lambda: self.__set_visible_table(self.managerExhibitionTableWidget, self.selectExhibitionTableAction)
        )
        self.setVisibleExcursionTableButton.clicked.connect(
            lambda: self.__set_visible_table(self.managerExcursionTableWidget, self.selectExcursionTableAction)
        )
        self.selectExcursionTableAction.changed.connect(
            lambda: self.__set_visible_table(self.managerExcursionTableWidget, self.selectExcursionTableAction)
        )

        self.exhibitionTable.itemSelectionChanged.connect(
            lambda: self.__focus_change([self.editExhibitionButton,
                                         self.addExhibitionTableAction,
                                         self.deleteExhibitionTableAction],

                                        [self.editExcursionButton,
                                         self.addExcursionAction,
                                         self.removeExcursionAction])
        )
        self.exhibitionTable.itemSelectionChanged.connect(
            self.exhibitionTable.clearSelection
        )

        self.excursionTable.itemSelectionChanged.connect(
            lambda: self.__focus_change([self.editExcursionButton,
                                         self.addExcursionAction,
                                         self.removeExcursionAction],

                                        [self.editExhibitionButton,
                                         self.addExhibitionTableAction,
                                         self.deleteExhibitionTableAction]
                                        )
        )
        self.excursionTable.itemSelectionChanged.connect(
            lambda: self.excursionTable.clearSelection()
        )

        self.addExhibitionButton.clicked.connect(
            lambda: self.form_dialog("Добавить выставку", "Добавить", "Выставка",
                                     operation=self.add_exhibition, table=self.exhibitionTable, is_new_row=True)
        )
        self.addExhibitionTableAction.triggered.connect(
            lambda: self.form_dialog("Добавить выставку", "Добавить", "Выставка",
                                     operation=self.add_exhibition, table=self.exhibitionTable, is_new_row=True)
        )

        self.editExhibitionButton.clicked.connect(
            lambda: self.form_dialog("Изменить информацию о выставке", "Изменить", "Выставка",
                                     operation=self.add_exhibition, table=self.exhibitionTable, is_new_row=False)
        )

        self.addExcursionButton.clicked.connect(
            lambda: self.form_dialog("Добавить экскурсию", "Добавить", "Экскурсия",
                                     operation=self.add_excursion, table=self.excursionTable, is_new_row=True)
        )
        self.addExcursionAction.triggered.connect(
            lambda: self.form_dialog("Добавить экскурсию", "Добавить", "Экскурсия",
                                     operation=self.add_excursion, table=self.excursionTable, is_new_row=True)
        )

        self.editExcursionButton.clicked.connect(
            lambda: self.form_dialog("Изменить информацию об экскурсии", "Изменить", "Экскурсия",
                                     operation=self.edit_excursion, table=self.excursionTable, is_new_row=False)
        )

        self.openExhibitionCalendarButton.clicked.connect(self.open_calendar)

        self.__quit_session_signal = parent_signal
        self.quitSessionAction.triggered.connect(
            lambda: self.__quit_session_signal.signal.emit()
        )

    @staticmethod
    def __set_visible_table(table: QWidget, action: QAction):
        table_visible: bool = table.isVisible()
        action_status: bool = action.isChecked()
        if table_visible == action_status:
            action.setChecked(not action_status)
        table.setHidden(table_visible)

    @staticmethod
    def __focus_change(focused_widgets: list[QWidget], unfocused_widgets: list[QWidget]):
        print("CPU")
        for widget in focused_widgets:
            widget.setEnabled(True)
        for widget in unfocused_widgets:
            widget.setEnabled(False)

    def form_dialog(self,
                    window_title: str,
                    button_label: str,
                    table_name: str,
                    operation: Callable,
                    table: MuseTableWidget,
                    is_new_row: bool):
        dialog_factory: DialogFormFactory = DialogFormFactory(window_title, button_label, table_name,
                                                              table.get_row_data(is_new_row))
        send_data_signal = TupleEmitter(self)
        send_data_signal.signal.connect(operation)
        dialog_form: MuseDialogWidget = dialog_factory(send_data_signal)
        dialog_form.show()
        dialog_form.exec_()

    def add_exhibition(self, dialog_output: tuple[str]):
        for i in range(self.exhibitionTable.columnCount()):
            self.exhibitionTable.setItem(self.exhibitionTable.rowCount() - 1, i, QTableWidgetItem(dialog_output[i]))

    def edit_exhibition(self, dialog_output: tuple[str]):
        for i in range(self.exhibitionTable.columnCount()):
            self.exhibitionTable.setItem(self.exhibitionTable.currentRow(), i, QTableWidgetItem(dialog_output[i]))

    def add_excursion(self, dialog_output: tuple[str]):
        for i in range(self.excursionTable.columnCount()):
            self.excursionTable.setItem(self.excursionTable.rowCount() - 1, i, QTableWidgetItem(dialog_output[i]))

    def edit_excursion(self, dialog_output: tuple[str]):
        for i in range(self.excursionTable.columnCount()):
            self.excursionTable.setItem(self.excursionTable.currentRow(), i, QTableWidgetItem(dialog_output[i]))

    def open_calendar(self):
        Form = QDialog(None)
        Form.setModal(True)
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        Form.exec_()
