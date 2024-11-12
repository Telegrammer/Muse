from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMainWindow, QAction, QWidget, QVBoxLayout

from src.CustomWidgets import *
from src.Emitters import VoidEmitter
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
            lambda: self.edit_row(
                [(self.exhibitTable.horizontalHeaderItem(i).text(),
                  self.exhibitTable.item(self.exhibitTable.currentRow(), i).text())
                 for i in range(self.exhibitTable.columnCount())
                 ], "Экспонат")
        )
        self.editEmployeeButton.clicked.connect(
            lambda: self.edit_row(
                [(self.employeeTable.horizontalHeaderItem(i).text(),
                  self.employeeTable.item(self.employeeTable.currentRow(), i).text())
                 for i in range(self.employeeTable.columnCount())
                 ], "данные сотрудника")
        )
        self.addEmployeeButton.clicked.connect(self.add_employee)
        self.addEmployeeAction.triggered.connect(self.add_employee)

        self.__quit_session_signal = parent_signal
        self.quitSessionAction.triggered.connect(
            lambda: self.__quit_session_signal.signal.emit()
        )

    @staticmethod
    def __set_visible_table(table: QWidget, action: QAction):
        table_visible: bool = table.isHidden()
        action_status: bool = action.isChecked()
        if table_visible == action_status:
            action.setChecked(not action_status)
        table.setHidden(not table_visible)

    @staticmethod
    def __focus_change(focused_widgets: list[QWidget], unfocused_widgets: list[QWidget]):
        for widget in focused_widgets:
            widget.setEnabled(True)
        for widget in unfocused_widgets:
            widget.setEnabled(False)

    @staticmethod
    def edit_row(row_data: list[tuple[str]], table_name: str):
        edit_form = MuseDialog(QSize(800, 600), "editExhibitForm")
        vertical_layout = QVBoxLayout(edit_form)
        edit_form.setWindowTitle(f"Изменить {table_name}")
        for header, data in row_data:
            vertical_layout.addWidget(MuseLabel(header, f"label {header}", edit_form))
            line_edit = MuseLineEdit(f"lineEdit {header}", edit_form)
            line_edit.setText(data)
            vertical_layout.addWidget(line_edit)

        vertical_layout.addWidget(MuseButton("Изменить", f"confirmButton", edit_form))

        edit_form.setModal(True)
        edit_form.show()
        edit_form.exec_()

    def add_employee(self):
        edit_form = MuseDialog(QSize(800, 600), "editExhibitForm")
        vertical_layout = QVBoxLayout(edit_form)
        headers = [self.employeeTable.horizontalHeaderItem(i).text() for i in range(self.employeeTable.columnCount())]
        edit_form.setWindowTitle(f"Добавить сотрудника")
        for header in headers:
            vertical_layout.addWidget(MuseLabel(header, f"label {header}", edit_form))
            vertical_layout.addWidget(MuseLineEdit(f"lineEdit {header}", edit_form))

        vertical_layout.addWidget(MuseButton("Добавить", f"confirmButton", edit_form))

        edit_form.setModal(True)
        edit_form.show()
        edit_form.exec_()
