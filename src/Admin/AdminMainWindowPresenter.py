from typing import Callable

from PyQt5.QtWidgets import QMainWindow, QAction, QWidget, QTableWidget, QDialog, QTableWidgetItem

from src.DialogFormFactory import DialogFormFactory
from src.Emitters import VoidEmitter, TupleEmitter
from .AdminMainWindowView import AdministratorMainWindowView

__all__ = ["AdminMainWindow"]


class AdminMainWindow(QMainWindow, AdministratorMainWindowView):

    def __init__(self, parent_signal: VoidEmitter):
        QMainWindow.__init__(self, None)
        self.setupUi(self)

        self.setVisibleEmployeeTableButton.clicked.connect(
            lambda: self.__set_visible_table(self.adminEmployeeTable, self.selectEmployeeTableAction_)
        )
        self.selectEmployeeTableAction_.changed.connect(
            lambda: self.__set_visible_table(self.adminEmployeeTable, self.selectEmployeeTableAction_)
        )
        self.setVisibleExhibitTableButton.clicked.connect(
            lambda: self.__set_visible_table(self.adminExhibitTable, self.selectExhibitAction)
        )
        self.selectExhibitAction.changed.connect(
            lambda: self.__set_visible_table(self.adminExhibitTable, self.selectExhibitAction)
        )

        self.employeeTable.itemSelectionChanged.connect(
            lambda: self.__focus_change([self.editEmployeeButton,
                                         self.addEmployeeAction,
                                         self.removeEmployeeAction],
                                        [self.editExhibitButton])
        )
        self.employeeTable.itemSelectionChanged.connect(
            self.exhibitTable.clearSelection
        )

        self.exhibitTable.itemSelectionChanged.connect(
            lambda: self.__focus_change([self.editExhibitButton], [self.editEmployeeButton,
                                                                   self.addEmployeeAction,
                                                                   self.removeEmployeeAction])
        )
        self.exhibitTable.itemSelectionChanged.connect(
            lambda: self.employeeTable.clearSelection()
        )

        self.editExhibitButton.clicked.connect(
            lambda: self.form_dialog("Изменить данные об экспонате", "Изменить", "Экспонат",
                                     operation=self.edit_exhibit, table=self.exhibitTable)
        )
        self.editEmployeeButton.clicked.connect(
            lambda: self.form_dialog("Изменить данные о сотруднике", "Изменить", "Сотрудник",
                                     operation=self.edit_employee, table=self.employeeTable)
        )
        self.addEmployeeButton.clicked.connect(
            lambda: self.form_dialog("Добавить сотрудника", "Добавить", "Сотрудник",
                                     operation=self.add_employee, table=self.employeeTable)
        )
        self.addEmployeeAction.triggered.connect(
            lambda: self.form_dialog("Добавить сотрудника", "Добавить", "Сотрудник",
                                     operation=self.add_employee, table=self.employeeTable)
        )

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

    def edit_exhibit(self, dialog_output: tuple[str]):
        for i in range(self.exhibitTable.columnCount()):
            self.exhibitTable.setItem(self.exhibitTable.currentRow(), i, QTableWidgetItem(dialog_output[i]))

    def edit_employee(self, dialog_output: tuple[str]):
        for i in range(self.employeeTable.columnCount()):
            self.employeeTable.setItem(self.employeeTable.currentRow(), i, QTableWidgetItem(dialog_output[i]))

    def add_employee(self, dialog_output: tuple[str]):
        self.employeeTable.insertRow(self.employeeTable.rowCount())
        for i in range(self.employeeTable.columnCount()):
            self.employeeTable.setItem(self.employeeTable.rowCount() - 1, i, QTableWidgetItem(dialog_output[i]))
