from PyQt5.QtCore import QObject, QSize, QDate
from PyQt5.QtWidgets import QDateEdit

from src.Emitters import StringEmitter
from src.SharedWidgets.MuseDataSource import MuseDataSource


class MuseDateEditView(object):

    def setup_ui(self, parent: QObject = None):
        parent.setMinimumSize(QSize(0, 30))
        parent.setStyleSheet("font: 87 8pt \"Arial Black\";\n"
                                               "\n"
                                               "border: 1px solid;\n"
                                               "border-radius:  5px;\n"
                                               "")


class MuseDateEdit(QDateEdit, MuseDateEditView, MuseDataSource):

    def __init__(self, parent: QObject = None, parent_signal: StringEmitter = StringEmitter(None)):
        QDateEdit.__init__(self, parent)
        self.setup_ui(self)
        self.__parent_signal = parent_signal

    def get_data(self):
        selected_date: str = f"'{self.text()}'"
        return selected_date

    def return_data_before_destroy(self):
        self.__parent_signal.signal.emit(self.get_data())

