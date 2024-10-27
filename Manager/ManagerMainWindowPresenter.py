from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget

from .ManagerMainWindowView import ManagerMainWindowView

__all__ = ["ManagerMainWindow"]


class ManagerMainWindow(QMainWindow, ManagerMainWindowView):

    def __init__(self, parent: QObject):
        QWidget.__init__(self, parent)
        self.setupUi(self)
