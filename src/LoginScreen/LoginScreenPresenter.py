from typing import Callable

import psycopg2
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget

from src.Admin.AdminMainWindowPresenter import AdminMainWindow
from src.Curator.CuratorMainWindowPresenter import CuratorMainWindow
from src.DataBase.GLOBALS import generate_hash
from src.Donator.DonatorMainWindowPresenter import DonatorMainWindow
from src.Emitters import TupleEmitter, VoidEmitter, StringEmitter
from src.Handler import HideWidgetsHandler, AlertMessageBox
from src.Manager.ManagerMainWindowPresenter import ManagerMainWindow
from src.SharedWidgets.Profile.DonatorProfile import DonatorProfilePresenter
from .LoginScreenRepository import LoginScreenRepository
from .LoginScreenView import LoginScreenView
from .RoleDecisionWidget import RoleDecisionWidget

__all__ = ["LoginScreen"]


class MainWindowFactory:

    def __init__(self, user_data):
        self.__user_data = user_data

        self.__tokens: dict[str, Callable[[QWidget], QMainWindow]] = {
            "менеджер": self.create_manager_window(),
            "администратор": self.create_admin_window(),
            "куратор": self.create_curator_window(),
            "даритель": self.create_donator_window(),
            "смотритель": self.pass_func(),
            "экскурсовод": self.pass_func()
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
        self.signInButton.clicked.connect(self.start_registrate)
        self.__login = ''
        self.__password = None

    def start_registrate(self):
        receive_signal = TupleEmitter(None)
        receive_signal.signal.connect(self.display_registration_data)
        registration_window = DonatorProfilePresenter(["", "", "", "", ""], parent_signal=receive_signal)
        registration_window.changeButton.setText("Зарегестрироваться")
        registration_window.setModal(True)
        registration_window.show()
        registration_window.exec_()

    def display_registration_data(self, dialog_output):
        self.loginLineEdit.setText(dialog_output[0])
        self.passwordLineEdit.setText(dialog_output[1])

    def create_main_window(self):
        self.__login: str = self.loginLineEdit.text()
        self.__password: str = "null"
        password_text = self.passwordLineEdit.text()
        if password_text != "":
            self.__password = psycopg2.Binary(generate_hash(password_text))

        status: str = LoginScreenRepository().authenticate_user(self.__login, self.__password)
        if status == 'Найдено несколько пользователей':
            role_signal = StringEmitter(self)
            role_signal.signal.connect(self.start_session)
            dialog_window = RoleDecisionWidget(None, role_signal)
            dialog_window.exec_()
            return

        if status not in LoginScreenRepository.get_roles():
            AlertMessageBox(None, "Ошибка аутентификации", 'Неверный логин или пароль')
            return
        self.start_session(status)

    def start_session(self, status: str):
        user_data: list = list(LoginScreenRepository().authorize_user(status, self.__login, self.__password))
        user_data.append(self.passwordLineEdit.text())
        factory: MainWindowFactory = MainWindowFactory(tuple(user_data))
        if status == "даритель":
            window, quit_session_signal = factory.create_main_window(status)
            self.__handler.add_widget(window, quit_session_signal)
            self.__handler.activation_change(self)
            return
        if user_data[2] in ["куратор", "менеджер", "администратор"]:
            window, quit_session_signal = factory.create_main_window(user_data[2])
            self.__handler.add_widget(window, quit_session_signal)
            self.__handler.activation_change(self)
            return
