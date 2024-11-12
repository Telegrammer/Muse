from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget

from .ManagerMainWindowView import ManagerMainWindowView
from src.Emitters import VoidEmitter

__all__ = ["ManagerMainWindow"]


class ManagerMainWindow(QMainWindow, ManagerMainWindowView):

    def __init__(self, parent_signal: VoidEmitter):
        QWidget.__init__(self, None)
        self.setupUi(self)

        self.__quit_session_signal = parent_signal
        self.quitSessionAction.triggered.connect(
            lambda: self.__quit_session_signal.signal.emit()
        )