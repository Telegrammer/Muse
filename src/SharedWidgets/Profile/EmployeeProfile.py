from enum import IntEnum

import psycopg2
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QDialog, QLineEdit, QMessageBox

from src.DataBase.DataBaseConnectionHelper import DataBaseConnectionHelper
from src.DataBase.GLOBALS import generate_hash
from src.Emitters import VoidEmitter
from src.SharedWidgets.Profile.EmployeeProfileView import ProfileWindowView
from src.Handler import AlertMessageBox
from src.AbstractRepository import AbstractRepository

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
        self.changePasswordButton.clicked.connect(self.change_password)
        self.user_data = user_data

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

    @AbstractRepository.handle_database_errors
    def change_password(self):
        if self.passwordLineEdit.text() != self.confirmPasswordLineEdit.text():
            AlertMessageBox(None, 'Ошибка!', 'Пароли не совпадают')
        else:
            connection = DataBaseConnectionHelper().connect()
            cursor = connection.cursor()

            cursor.execute(
                f"call changeEmployeePassword({self.user_data[0]}, {psycopg2.Binary(generate_hash(self.passwordLineEdit.text()))});")
            connection.commit()
            cursor.close()
            connection.close()

            AlertMessageBox(None, 'Успешно', 'Пароль изменен')
