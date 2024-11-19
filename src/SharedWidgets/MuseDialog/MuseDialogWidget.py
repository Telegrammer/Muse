from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout

from src.SharedWidgets.MuseDataSource import MuseDataSource
from ..MuseButton import MuseButton
from ...Emitters import TupleEmitter


class MuseDialogView(object):

    def setup_ui(self, dialog_window: QDialog, size: QSize):
        dialog_window.resize(size)
        dialog_window.setStyleSheet("QMenuBar {\n"
                                    "background-color: rgb(250, 234, 153);\n"
                                    "font: 87 10pt \"Arial Black\";\n"
                                    "padding-left: 3px;\n"
                                    "    color: rgb(82, 30, 1);\n"
                                    "}\n"
                                    "\n"
                                    "QMenuBar::item {\n"
                                    "spacing: 3px; /* spacing between menu bar items */\n"
                                    "padding: 1px 4px;\n"
                                    "background: transparent;\n"
                                    "border-radius: 4px;\n"
                                    "background-color: rgb(250, 234, 153);\n"
                                    "}\n"
                                    "\n"
                                    "QMenuBar::item:selected { /* when selected using mouse or keyboard */\n"
                                    "background: #fac983;\n"
                                    "}\n"
                                    "\n"
                                    "QMenu {\n"
                                    "background-color: rgb(149, 166, 174); \n"
                                    "    font: 75 8pt \"Arial Black\";\n"
                                    "}\n"
                                    "\n"
                                    "QMenu::item {\n"
                                    "background-color: transparent;\n"
                                    "}\n"
                                    "\n"
                                    "QMenu::item:selected {\n"
                                    "background-color: #fac983; /* rot */\n"
                                    "}\n"
                                    "QWidget{background-color: rgb(255, 253, 223);}")


class MuseDialog(QDialog, MuseDialogView):
    def __init__(self, size: QSize, parent_signal: TupleEmitter):
        QDialog.__init__(self, None)
        self.setup_ui(self, size)
        self.__confirm_button = MuseButton("", self)
        self.__data_sources: list[MuseDataSource] = []
        self.__data_transfer = parent_signal
        self.__confirm_button.clicked.connect(self.__send_data)
        self.__layout: QVBoxLayout = None

    def __send_data(self):
        self.__data_transfer.signal.emit(tuple(data_source.get_data() for data_source in self.__data_sources))
        self.close()

    def get_confirm_button(self) -> QPushButton:
        return self.__confirm_button

    def set_layout(self, layout: QVBoxLayout):
        self.__layout = layout

    def get_layout(self):
        return self.__layout

    def add_data_source(self, data_source: MuseDataSource):
        self.__data_sources.append(data_source)
