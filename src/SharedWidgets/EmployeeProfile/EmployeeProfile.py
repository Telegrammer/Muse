from enum import IntEnum

from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QDialog, QLineEdit

from src.Emitters import VoidEmitter
from src.SharedWidgets.EmployeeProfile.EmployeeProfileView import ProfileWindowView


class EmployeeProfilePresenter(QDialog, ProfileWindowView):
    class UserData(IntEnum):
        id = 0
        fullname = 1
        position = 2
        birthDate = 3
        phoneNumber = 4
        password = 5

    def __init__(self, user_data: tuple, parent: QObject = None, parent_signal=VoidEmitter(None)):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.__parent_signal = parent_signal
        self.nameLineEdit.setText(user_data[self.UserData.fullname])
        self.birthDateEdit.setDate(user_data[self.UserData.birthDate])
        self.positionLabel.setText(self.positionLabel.text() + " " + user_data[self.UserData.position])
        self.phoneLineEdit.setText(user_data[self.UserData.phoneNumber])
        self.passwordLineEdit.setText(user_data[self.UserData.password])
        self.closeProfileButton.clicked.connect(self.close)
        self.passwordLineEdit.textChanged.connect(self.prepare_change_password)
        self.passwordVisibleCheckBox.stateChanged.connect(self.set_password_visible)

    def prepare_change_password(self):
        self.confirmPasswordLineEdit.setEnabled(True)
        self.changePasswordButton.setEnabled(True)

    def set_password_visible(self):
        if not self.passwordVisibleCheckBox.isChecked():
            self.passwordLineEdit.setEchoMode(QLineEdit.Password)
            self.confirmPasswordLineEdit.setEchoMode(QLineEdit.Password)
        else:
            self.passwordLineEdit.setEchoMode(QLineEdit.Normal)
            self.confirmPasswordLineEdit.setEchoMode(QLineEdit.Normal)
