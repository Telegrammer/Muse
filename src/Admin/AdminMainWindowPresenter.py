from typing import Callable

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMainWindow, QAction, QWidget, QDialog, QCheckBox

from src.Emitters import VoidEmitter, TupleEmitter
from src.SharedWidgets.EmployeeProfile.EmployeeProfile import EmployeeProfilePresenter
from src.SharedWidgets.MuseDialog.DialogFormFactory import DialogFormFactory
from src.SharedWidgets.MuseDialog.MuseFindDialogWidget import MuseFindDialog
from .AdminMainWindowView import AdministratorMainWindowView
from .AdminRepository import AdminRepository, EmployeeData
from ..SharedWidgets.MuseTableWidget import MuseTableWidget

__all__ = ["AdminMainWindow"]


class AdminMainWindow(QMainWindow, AdministratorMainWindowView):

    def __init__(self, parent_signal: VoidEmitter, user_data: tuple):

        QMainWindow.__init__(self, None)
        self.setupUi(self)
        self.__user_data = user_data
        self.update_tables()
        self.__last_row = []

        # Employee

        self.viewProfileInfoAction.triggered.connect(self.open_profile)

        self.setVisibleEmployeeTableButton.clicked.connect(
            lambda: self.__set_visible_table(self.adminEmployeeTable, self.selectEmployeeTableAction_)
        )
        self.selectEmployeeTableAction_.changed.connect(
            lambda: self.__set_visible_table(self.adminEmployeeTable, self.selectEmployeeTableAction_)
        )

        self.employeeTable.itemSelectionChanged.connect(
            lambda: self.__focus_change([self.editEmployeeButton,
                                         self.addEmployeeAction,
                                         self.removeEmployeeAction,
                                         self.findEmployeeAction],
                                        [self.editExhibitButton, self.findExhibitAction])
        )

        self.employeeTable.cellDoubleClicked.connect(
            lambda: self.set_possible_change_row(self.employeeTable)
        )

        self.employeeTable.itemSelectionChanged.connect(
            lambda: self.clear_selection(self.exhibitTable)
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

        self.findEmployeeButton.clicked.connect(
            lambda: self.form_find_dialog(operation=self.find_employee, window_title="Найти сотрудника",
                                          table=self.employeeTable)
        )

        self.findEmployeeAction.triggered.connect(
            lambda: self.form_find_dialog(operation=self.find_employee, window_title="Найти сотрудника",
                                          table=self.employeeTable)
        )
        self.removeEmployeeButton.clicked.connect(self.remove_employee)

        self.sortEmployeeButton.clicked.connect(self.sort_employees)

        # Exhibit

        self.exhibitTable.itemSelectionChanged.connect(
            lambda: self.__focus_change([self.editExhibitButton, self.findExhibitAction], [self.editEmployeeButton,
                                                                                           self.addEmployeeAction,
                                                                                           self.removeEmployeeAction,
                                                                                           self.findEmployeeAction])
        )
        self.exhibitTable.itemSelectionChanged.connect(
            lambda: self.clear_selection(self.employeeTable)
        )

        self.editExhibitButton.clicked.connect(
            lambda: self.form_dialog("Изменить данные об экспонате", "Изменить", "Экспонат",
                                     operation=self.edit_exhibit, table=self.exhibitTable, is_new_row=False)
        )

        self.findExhibitButton.clicked.connect(
            lambda: self.form_find_dialog("Найти экспонаты", operation=self.find_exhibit,
                                          table=self.exhibitTable)
        )
        self.findExhibitAction.triggered.connect(
            lambda: self.form_find_dialog("Найти экспонаты", operation=self.find_exhibit,
                                          table=self.exhibitTable)
        )

        self.setVisibleExhibitTableButton.clicked.connect(
            lambda: self.__set_visible_table(self.adminExhibitTable, self.selectExhibitAction)
        )
        self.selectExhibitAction.changed.connect(
            lambda: self.__set_visible_table(self.adminExhibitTable, self.selectExhibitAction)
        )

        self.sortExhibitButton.clicked.connect(self.sort_exhibits)

        # quit session

        self.__quit_session_signal = parent_signal
        self.quitSessionAction.triggered.connect(
            lambda: self.__quit_session_signal.signal.emit()
        )

    def open_profile(self):

        profile_window = EmployeeProfilePresenter(self.__user_data, self)
        profile_window.setModal(True)
        profile_window.show()
        profile_window.exec_()

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

    def clear_selection(self, table: MuseTableWidget):
        table.clearSelection()

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

    def set_possible_change_row(self, table: MuseTableWidget):
        self.__last_row = table.get_row_data(is_new_row=False)

    def edit_employee(self, dialog_output: tuple[str]):
        try:
            AdminRepository().edit_employee(dialog_output[EmployeeData.fullname],
                                            dialog_output[EmployeeData.position],
                                            dialog_output[EmployeeData.birthDate],
                                            dialog_output[EmployeeData.phoneNumber],
                                            self.employeeTable.get_id(self.employeeTable.currentRow()))
        except IndexError:
            pass
        finally:
            self.update_employee_table()

    def add_employee(self, dialog_output: tuple[str]):
        self.employeeTable.insertRow(self.employeeTable.rowCount())
        AdminRepository().add_employee(dialog_output[0], dialog_output[1], dialog_output[2], dialog_output[3])
        self.update_employee_table()

    def remove_employee(self):
        AdminRepository().remove_employee(self.employeeTable.get_id(self.employeeTable.currentRow()))
        self.update_employee_table()

    def form_find_dialog(self, window_title: str, operation: Callable, table: MuseTableWidget):
        send_data_signal = TupleEmitter(self)
        send_data_signal.signal.connect(operation)
        find_dialog_form = MuseFindDialog(QSize(800, 600), table.get_attributes(), send_data_signal)
        find_dialog_form.setWindowTitle(window_title)
        find_dialog_form.setModal(True)
        find_dialog_form.exec_()

    def find_employee(self, dialog_output: tuple[str]):
        self.employeeTable.set_filters(dialog_output)
        self.update_employee_table(dialog_output)

    def sort_employees(self):

        button_group: list[QWidget] = self.sortTypeEmployeeButtonGroup.buttons()
        is_ascending: bool = self.empRadioButtonAscending.isChecked()
        order_filters: list[tuple[str, bool]] = []
        for i in range(len(button_group)):
            check_box: QCheckBox = button_group[i]
            if not check_box.isChecked():
                continue
            order_filters.append((check_box.text().replace(" ", ""), is_ascending))
        self.update_employee_table(filters=self.employeeTable.get_filters(), orders=order_filters)

    def edit_exhibit(self, dialog_output: tuple[str]):
        try:
            row_data = self.exhibitTable.get_row_data()

            attributes = [(dialog_output[i], row_data[i][1]) for i in range(len(row_data))]
            AdminRepository().edit_exhibit(attributes,
                                           exhibit_id=self.exhibitTable.get_id(self.exhibitTable.currentRow()))

        except IndexError:
            pass
        finally:
            self.update_exhibit_table()

    def find_exhibit(self, dialog_output: tuple[str]):
        self.exhibitTable.set_filters(dialog_output)
        self.update_exhibit_table(dialog_output)

    def sort_exhibits(self):

        button_group: list[QWidget] = self.sortTypeExhibitButtonGroup.buttons()
        is_ascending: bool = self.exRadioButtonAscending.isChecked()
        order_filters: list[tuple[str, bool]] = []
        for i in range(len(button_group)):
            check_box: QCheckBox = button_group[i]
            if not check_box.isChecked():
                continue
            order_filters.append((check_box.text().replace(" ", ""), is_ascending))
        self.update_exhibit_table(filters=self.employeeTable.get_filters(), orders=order_filters)

    def update_employee_table(self, filters=None, orders=None):
        self.employeeTable.blockSignals(True)
        self.employeeTable.setRowCount(0)
        self.employeeTable.clear_ids()
        employees = AdminRepository().find_employees(sender_phone_number=self.__user_data[EmployeeData.phoneNumber],
                                                     attributes=filters, orders=orders)
        for employee in employees:
            self.employeeTable.insertRow(self.employeeTable.rowCount())
            self.employeeTable.add_id(employee[0])
            self.employeeTable.set_row(employee[1:])
        self.employeeTable.set_attribute_values("Должность", AdminRepository().get_employees_positions())
        self.employeeTable.blockSignals(False)
        self.__focus_change([], [self.editEmployeeButton, self.addEmployeeAction, self.findEmployeeAction,
                                 self.removeEmployeeAction])

    def update_exhibit_table(self, filters=None, orders=None):
        self.exhibitTable.blockSignals(True)
        self.exhibitTable.setRowCount(0)
        self.exhibitTable.clear_ids()
        exhibits = AdminRepository().find_exhibits(attributes=filters, orders=orders)
        for exhibit in exhibits:
            self.exhibitTable.insertRow(self.exhibitTable.rowCount())
            self.exhibitTable.add_id(exhibit[0])
            self.exhibitTable.set_row(exhibit[1:])
        self.exhibitTable.set_attribute_values("Вид", AdminRepository().get_exhibit_types())
        self.exhibitTable.set_attribute_values("Номер зала", AdminRepository().get_exhibit_halls())
        self.exhibitTable.set_attribute_values("Состояние", AdminRepository().get_exhibit_statuses())
        self.exhibitTable.blockSignals(False)
        self.__focus_change([], [self.editExhibitButton])

    def update_tables(self):
        self.update_employee_table()
        self.update_exhibit_table()
