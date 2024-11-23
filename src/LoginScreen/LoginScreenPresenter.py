from typing import Callable

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget

from src.Admin.AdminMainWindowPresenter import AdminMainWindow
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
            "даритель": self.create_donator_window()
        }
    @staticmethod
    def create_donator_window():
        pass

    def create_main_window(self, user_type: str):
        return self.__tokens[user_type]

    def create_manager_window(self):
        quit_session_signal = VoidEmitter(None)
        return ManagerMainWindow(quit_session_signal), quit_session_signal

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
        status: str = LoginScreenRepository.authenticate_user(login)
        if status not in LoginScreenRepository.get_roles():
            return

        user_data: tuple = LoginScreenRepository.authorize_user(status, login)
        print(user_data)
        factory: MainWindowFactory = MainWindowFactory(user_data)
        if status == "даритель":
            window, quit_session_signal = factory.create_main_window(status)
        else:
            window, quit_session_signal = factory.create_main_window(user_data[1])

        self.__handler.add_widget(window, quit_session_signal)
        self.__handler.activation_change(self)
