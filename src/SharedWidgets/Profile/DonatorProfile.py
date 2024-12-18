from enum import IntEnum

import psycopg2
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QDialog, QLineEdit

from src.AbstractRepository import AbstractRepository
from src.DataBase.DataBaseConnectionHelper import DataBaseConnectionHelper
from src.DataBase.GLOBALS import generate_hash
from src.Emitters import TupleEmitter
from src.Handler import AlertMessageBox
from src.SharedWidgets.Profile.DonatorProfileView import ProfileWindowView


class DonatorProfilePresenter(QDialog, ProfileWindowView):
    class UserData(IntEnum):
        id = 0
        fullname = 1
        phoneNumber = 2
        email = 3
        password = 4

    def __init__(self, user_data: tuple, parent: QObject = None, parent_signal=TupleEmitter(None)):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.__parent_signal = parent_signal
        self.nameLineEdit.setText(user_data[self.UserData.fullname])
        self.phoneLineEdit.setText(user_data[self.UserData.phoneNumber])
        self.emailEdit.setText(user_data[self.UserData.email])
        self.passwordLineEdit.setText(user_data[self.UserData.password])
        self.closeProfileButton.clicked.connect(self.close)
        self.passwordLineEdit.textChanged.connect(self.prepare_change_password)
        self.passwordVisibleCheckBox.stateChanged.connect(self.set_password_visible)
        self.changeButton.clicked.connect(self.identify_operation)
        self.user_data = user_data

    def prepare_change_password(self):
        self.confirmPasswordLineEdit.setEnabled(True)
        self.changeButton.setEnabled(True)

    def set_password_visible(self):
        if not self.passwordVisibleCheckBox.isChecked():
            self.passwordLineEdit.setEchoMode(QLineEdit.Password)
            self.confirmPasswordLineEdit.setEchoMode(QLineEdit.Password)
        else:
            self.passwordLineEdit.setEchoMode(QLineEdit.Normal)
            self.confirmPasswordLineEdit.setEchoMode(QLineEdit.Normal)

    def identify_operation(self):
        if self.passwordLineEdit.text() != self.confirmPasswordLineEdit.text():
            AlertMessageBox(None, 'Ошибка!', 'Пароли не совпадают')
            return
        if self.changeButton.text() == 'Зарегестрироваться':
            self.registrate_user()
            return

        self.update_donator_data()

    @AbstractRepository.handle_database_errors
    def registrate_user(self):
        connection = DataBaseConnectionHelper().connect()
        cursor = connection.cursor()

        cursor.execute(
            f"call registrateUser('{self.nameLineEdit.text()}', '{self.phoneLineEdit.text()}', '{self.emailEdit.text()}',"
            f"                    {psycopg2.Binary(generate_hash(self.passwordLineEdit.text()))});")
        connection.commit()
        cursor.close()
        connection.close()
        AlertMessageBox(None, "Успешно", "Вы зарегестрированы")
        self.close()

    @AbstractRepository.handle_database_errors
    def update_donator_data(self):

        connection = DataBaseConnectionHelper().connect()
        cursor = connection.cursor()

        cursor.execute(
            f"call updateDonatorData({self.user_data[0]}, '{self.nameLineEdit.text()}',"
            f" '{self.phoneLineEdit.text()}', '{self.emailEdit.text()}',"
            f"  {psycopg2.Binary(generate_hash(self.passwordLineEdit.text()))});")
        connection.commit()
        cursor.close()
        connection.close()
        AlertMessageBox(None, "Успешно", "Профиль изменен")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = DonatorProfilePresenter(["d", "d", "d", "d", "d"])
    Dialog.show()
    sys.exit(app.exec_())
