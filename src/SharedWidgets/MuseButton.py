from PyQt5.QtCore import QObject, QSize
from PyQt5.QtWidgets import QPushButton, QSizePolicy

from src.SharedWidgets.MuseDataSource import MuseDataSource, StringEmitter

__all__ = ["MuseButton"]


class MuseButtonView(object):

    def setup_ui(self, text: str, button: QPushButton):
        size_policy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
        button.setSizePolicy(size_policy)
        button.setStyleSheet("QWidget {\n"
                             "    background-color: rgb(250, 234, 153);\n"
                             "    border: 1px solid rgb(250, 201, 131);\n"
                             "    border-radius: 10px;\n"
                             "    text-align: center;\n"
                             "}\n"
                             "\n"
                             "QAbstractButton {\n"
                             "    \n"
                             "    font: 87 8pt \"Arial Black\";\n"
                             "    color: rgb(82, 30, 1);\n"
                             "}\n"
                             "QPushButton:hover:!pressed {\n"
                             "  border: 2px solid rgb(250, 201, 131);\n"
                             "}"
                             "QPushButton:!enabled {\n"
                             "    \n"
                             "    background: rgba(160, 160, 160, 100);\n"
                             "    font: 87 8pt \"Arial Black\";\n"
                             "    border: 1px solid rgb(150, 150, 150);\n"
                             "    border-radius: 10px;\n"
                             "    color: rgba(82, 30, 1, 100);\n"
                             "}")

        button.setMinimumSize(QSize(len(text) * 8, 31))
        button.setMaximumSize(QSize(16777215, 31))
        button.setText(text)


class MuseButton(QPushButton, MuseButtonView, MuseDataSource):

    def __init__(self, text: str, parent: QObject = None, parent_signal: StringEmitter = StringEmitter(None)):
        QPushButton.__init__(self, parent)
        self.setup_ui(text, self)
        self.__parent_signal = parent_signal

    def get_data(self):
        return self.text()

    def return_data_before_destroy(self):
        self.__parent_signal.signal.emit(self.get_data())
