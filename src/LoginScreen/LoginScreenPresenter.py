from typing import Callable

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget

from src.Admin.AdminMainWindowPresenter import AdminMainWindow
from src.Manager.ManagerMainWindowPresenter import ManagerMainWindow
from .LoginScreenView import LoginScreenView
from src.Handler import HideWidgetsHandler
from src.Emitters import VoidEmitter

__all__ = ["LoginScreen"]


class MainWindowFactory:

    def __init__(self):
        self.__tokens: dict[str, Callable[[QWidget], QMainWindow]] = {
            "менеджер": self.create_manager_window(),
            "администратор": self.create_admin_window()
        }

    def create_main_window(self, user_type: str):
        return self.__tokens[user_type]

    @staticmethod
    def create_manager_window():
        quit_session_signal = VoidEmitter(None)
        return ManagerMainWindow(quit_session_signal), quit_session_signal

    @staticmethod
    def create_admin_window():
        quit_session_signal = VoidEmitter(None)
        return AdminMainWindow(quit_session_signal), quit_session_signal


class LoginScreen(QWidget, LoginScreenView):

    def __init__(self):
        QWidget.__init__(self, None)
        self.setupUi(self)

        self.logInButton.clicked.connect(self.create_main_window)
        self.__handler = HideWidgetsHandler(self)

    def create_main_window(self):
        factory: MainWindowFactory = MainWindowFactory()
        window, quit_session_signal = factory.create_main_window(self.loginLineEdit.text().lower())
        self.__handler.add_widget(window, quit_session_signal)
        self.__handler.activation_change(self)

