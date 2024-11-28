from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QWidget

from src.Emitters import StringEmitter
from src.SharedWidgets.MuseDataSource import MuseDataSource
from src.SharedWidgets.MuseDateEdit import MuseDateEdit
from src.SharedWidgets.MuseLabel import MuseLabel


class MusePeriodWidget(QWidget, MuseDataSource):

    def __init__(self, parent: QObject = None, parent_signal: StringEmitter = StringEmitter(None)):
        QWidget.__init__(self, parent)
        self._layout = QHBoxLayout(self)

        self.startLabel = MuseLabel("От", self)
        self._layout.addWidget(self.startLabel)
        self.start = MuseDateEdit(self)
        self._layout.addWidget(self.start)

        self.endLabel = MuseLabel("До", self)
        self._layout.addWidget(self.endLabel)
        self.end = MuseDateEdit(self)
        self._layout.addWidget(self.end)

        self.__parent_signal = parent_signal


    def get_data(self):
        return f"between {self.start.get_data()} and {self.end.get_data()}"

    def return_data_before_destroy(self):
        self.__parent_signal.signal.emit(self.get_data())
