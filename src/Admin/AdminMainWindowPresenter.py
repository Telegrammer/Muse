from typing import Callable

from PyQt5.QtWidgets import QMainWindow, QAction, QWidget, QDialog, QTableWidgetItem

from src.Emitters import VoidEmitter, TupleEmitter
from src.SharedWidgets.MuseDialog.DialogFormFactory import DialogFormFactory
from .AdminMainWindowView import AdministratorMainWindowView
from ..SharedWidgets.MuseTableWidget import MuseTableWidget

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
                                         self.removeEmployeeAction,
                                         self.findEmployeeAction],
                                        [self.editExhibitButton, self.findExhibitAction])
        )
        self.employeeTable.itemSelectionChanged.connect(
            self.exhibitTable.clearSelection
        )

        self.exhibitTable.itemSelectionChanged.connect(
            lambda: self.__focus_change([self.editExhibitButton, self.findExhibitAction], [self.editEmployeeButton,
                                                                                           self.addEmployeeAction,
                                                                                           self.removeEmployeeAction,
                                                                                           self.findEmployeeAction])
        )
        self.exhibitTable.itemSelectionChanged.connect(
            lambda: self.employeeTable.clearSelection()
        )

        self.editExhibitButton.clicked.connect(
            lambda: self.form_dialog("Изменить данные об экспонате", "Изменить", "Экспонат",
                                     operation=self.edit_exhibit, table=self.exhibitTable, is_new_row=False)
        )
        self.editEmployeeButton.clicked.connect(
            lambda: self.form_dialog("Изменить данные о сотруднике", "Изменить", "Сотрудник",
                                     operation=self.edit_employee, table=self.employeeTable, is_new_row=False)
        )
        self.addEmployeeButton.clicked.connect(
            lambda: self.form_dialog("Добавить сотрудника", "Добавить", "Сотрудник",
                                     operation=self.add_employee, table=self.employeeTable, is_new_row=True)
        )
        self.addEmployeeAction.triggered.connect(
            lambda: self.form_dialog("Добавить сотрудника", "Добавить", "Сотрудник",
                                     operation=self.add_employee, table=self.employeeTable, is_new_row=True)
        )

        self.removeEmployeeButton.clicked.connect(self.employeeTable.get_row_range)

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

    def form_dialog(self,
                    window_title: str,
                    button_label: str,
                    table_name: str,
                    operation: Callable,
                    table: MuseTableWidget,
                    is_new_row: bool
                    ):
        dialog_factory: DialogFormFactory = DialogFormFactory(window_title, button_label, table_name,
                                                              table.get_row_data(is_new_row))
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

    def sort_exhibit_table(self):
        is_ascending: bool = self.exRadioButtonAscending.isChecked()
