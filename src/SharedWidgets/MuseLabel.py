from PyQt5.QtCore import QObject, QSize
from PyQt5.QtWidgets import QLabel, QSizePolicy

from src.SharedWidgets.MuseDataSource import MuseDataSource, StringEmitter

__all__ = ["MuseLabel"]


class MuseLabelView(object):

    def setup_ui(self, label_text: str, label: QLabel):
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
        label.setSizePolicy(sizePolicy)
        label.setMinimumSize(QSize(8 * len(label_text), 40))
        label.setStyleSheet("QLabel {\n"
                            "    font: 87 8pt \"Arial Black\";\n"
                            "    color: rgb(82, 30, 1);\n"
                            "}")
        label.setText(label_text)


class MuseLabel(QLabel, MuseLabelView, MuseDataSource):

    def __init__(self, label_text: str, parent: QObject = None, parent_signal: StringEmitter = StringEmitter(None)):
        QLabel.__init__(self, parent)
        self.setup_ui(label_text, self)
        self.__parent_signal = parent_signal

    def get_data(self):
        return self.text()

    def return_data_before_destroy(self):
        self.__parent_signal.signal.emit(self.get_data())
