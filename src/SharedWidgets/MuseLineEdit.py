from PyQt5.QtCore import QObject, QSize
from PyQt5.QtWidgets import QLineEdit

from src.SharedWidgets.MuseDataSource import MuseDataSource, StringEmitter

__all__ = ["MuseLineEdit"]


class MuseLineEditView(object):

    def setup_ui(self, line_edit: QLineEdit):
        line_edit.setMinimumSize(QSize(10, 31))
        line_edit.setMaximumSize(QSize(16777215, 31))
        line_edit.setStyleSheet("QLineEdit {\n"
                                "    \n"
                                "    font: 8pt \"Arial\";\n"
                                "    padding-left: 10px;\n"
                                "    padding-right: 10px;\n"
                                "    background-color: rgb(250, 235, 180);\n"
                                "    border-radius: 10px;\n"
                                "}\n"
                                "\n"
                                "QLineEdit:focus {\n"
                                "  border: 2px solid rgb(250, 201, 131);\n"
                                "}")


class MuseLineEdit(QLineEdit, MuseLineEditView, MuseDataSource):

    def __init__(self, parent: QObject = None, parent_signal: StringEmitter = StringEmitter(None)):
        QLineEdit.__init__(self, parent)
        self.setup_ui(self)
        self.__parent_signal = parent_signal

    def get_data(self):
        return self.text()

    def return_data_before_destroy(self):
        self.__parent_signal.signal.emit(self.get_data())