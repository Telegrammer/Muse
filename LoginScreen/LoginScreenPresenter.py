from typing import Callable

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget

from Admin.AdminMainWindowPresenter import AdminMainWindow
from Manager.ManagerMainWindowPresenter import ManagerMainWindow
from .LoginScreenView import LoginScreenView

__all__ = ["LoginScreen"]


class MainWindowFactory:

    def __init__(self, parent: QWidget):
        self.__parent = parent
        self.__tokens: dict[str, Callable[[QWidget], QMainWindow]] = {
            "менеджер": self.create_manager_window,
            "администратор": self.create_admin_window
        }

    def create_main_window(self, user_type: str = "менеджер"):
        return self.__tokens[user_type]

    def create_manager_window(self):
        return ManagerMainWindow(self.__parent)

    def create_admin_window(self):
        return AdminMainWindow(self.__parent)


class LoginScreen(QWidget, LoginScreenView):

    def __init__(self):
        QWidget.__init__(self, None)
        self.setupUi(self)

        self.logInButton.clicked.connect(self.create_main_window)

    def create_main_window(self):
        window: QMainWindow = MainWindowFactory(self).create_admin_window()
        window.show()
        self.hide()
