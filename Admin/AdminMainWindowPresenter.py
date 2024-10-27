from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QObject

from .AdminMainWindowView import AdministratorMainWindowView

__all__ = ["AdminMainWindow"]


class AdminMainWindow(QMainWindow, AdministratorMainWindowView):

    def __init__(self, parent: QObject):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.setVisibleEmployeeTableButton.clicked.connect(self.set_visible_employee_table)
        self.selectEmployeeTableAction_.changed.connect(self.set_visible_employee_table)
        self.setVisibleExhibitTableButton.clicked.connect(self.set_visible_exhibit_table)
        self.selectExhibitAction.changed.connect(self.set_visible_exhibit_table)
        self.quitSessionAction.triggered.connect(self.quit_session)

    def set_visible_employee_table(self):
        is_table_visible: bool = self.adminEmployeeTable.isHidden()
        is_action_checked: bool = self.selectEmployeeTableAction_.isChecked()
        if is_table_visible == is_action_checked:
            self.selectEmployeeTableAction_.setChecked(not self.selectEmployeeTableAction_.isChecked())
        self.adminEmployeeTable.setHidden(not is_table_visible)

    def set_visible_exhibit_table(self):
        is_table_visible: bool = self.adminExhibitTable.isHidden()
        is_action_checked: bool = self.selectExhibitAction.isChecked()
        if is_table_visible == is_action_checked:
            self.selectExhibitAction.setChecked(not self.selectExhibitAction.isChecked())
        self.adminExhibitTable.setHidden(not is_table_visible)

    def quit_session(self):
        self.parent().show()
        self.close()

