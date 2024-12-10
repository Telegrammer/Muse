from typing import Callable

import psycopg2
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtWidgets import QWidget

from src.Admin.AdminMainWindowPresenter import AdminMainWindow
from src.Curator.CuratorMainWindowPresenter import CuratorMainWindow
from src.DataBase.GLOBALS import generate_hash
from src.Donator.DonatorMainWindowPresenter import DonatorMainWindow
from src.Emitters import VoidEmitter
from src.Handler import HideWidgetsHandler
from src.Manager.ManagerMainWindowPresenter import ManagerMainWindow
from .LoginScreenRepository import LoginScreenRepository
from .LoginScreenView import LoginScreenView

__all__ = ["LoginScreen"]


class MainWindowFactory:

    def __init__(self, user_data):
        self.__user_data = user_data

        self.__tokens: dict[str, Callable[[QWidget], QMainWindow]] = {
            "менеджер": self.create_manager_window(),
            "администратор": self.create_admin_window(),
            "куратор": self.create_curator_window(),
            "даритель": self.create_donator_window(),
            "смотритель": self.pass_func()
        }

    def pass_func(self):
        pass

    def create_donator_window(self):
        quit_session_signal = VoidEmitter(None)
        return DonatorMainWindow(quit_session_signal, self.__user_data), quit_session_signal

    def create_main_window(self, user_type: str):
        return self.__tokens[user_type]

    def create_curator_window(self):
        quit_session_signal = VoidEmitter(None)
        return CuratorMainWindow(quit_session_signal, self.__user_data), quit_session_signal

    def create_manager_window(self):
        quit_session_signal = VoidEmitter(None)
        return ManagerMainWindow(quit_session_signal, self.__user_data), quit_session_signal

    def create_admin_window(self):
        quit_session_signal = VoidEmitter(None)

        return AdminMainWindow(quit_session_signal, self.__user_data), quit_session_signal


class LoginScreen(QWidget, LoginScreenView):

    def __init__(self):
        QWidget.__init__(self, None)
        self.setupUi(self)

        self.logInButton.clicked.connect(self.create_main_window)
        self.__handler = HideWidgetsHandler(self)

    def create_main_window(self):
        login: str = self.loginLineEdit.text()
        password_text: str = self.passwordLineEdit.text()
        if password_text is None or password_text == "":
            password = "null"
        else:
            password = psycopg2.Binary(generate_hash(password_text))
        status: str = LoginScreenRepository().authenticate_user(login, password)
        if status not in LoginScreenRepository.get_roles():
            error_window = QMessageBox()
            error_window.setWindowTitle("Ошибка аутентификации")
            error_window.setText('Неверный логин или пароль')
            error_window.setModal(True)
            error_window.show()
            error_window.exec_()
            return

        user_data: list = list(LoginScreenRepository().authorize_user(status, login, password))
        user_data.append(self.passwordLineEdit.text())
        print(user_data)
        factory: MainWindowFactory = MainWindowFactory(tuple(user_data))
        if status == "даритель":
            window, quit_session_signal = factory.create_main_window(status)
            self.__handler.add_widget(window, quit_session_signal)
            self.__handler.activation_change(self)
            return
        if user_data[2] != "смотритель":
            window, quit_session_signal = factory.create_main_window(user_data[2])
            self.__handler.add_widget(window, quit_session_signal)
            self.__handler.activation_change(self)
            return

        error_window = QMessageBox()
        error_window.setWindowTitle("Ошибка аутентификации")
        error_window.setText('Неверный логин или пароль')
        error_window.setModal(True)
        error_window.show()
        error_window.exec_()

