from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout

from src.SharedWidgets.MuseDataSource import MuseDataSource
from src.SharedWidgets.MuseButton import MuseButton
from src.Emitters import TupleEmitter
import sys
from PyQt5 import QtCore, QtWidgets

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
        self._confirm_button = MuseButton("", self)
        self._data_sources: list[MuseDataSource] = []
        self._data_transfer = parent_signal
        self._confirm_button.clicked.connect(self._send_data)
        self._layout: QVBoxLayout = None

    def _send_data(self):
        print(self._data_transfer)
        self._data_transfer.signal.emit(tuple(data_source.get_data() for data_source in self._data_sources))
        self.close()

    def remove_data_source(self, index: int):
        self._data_sources[index].setHidden(True)
        self._data_sources.pop(index)

    def get_confirm_button(self) -> QPushButton:
        return self._confirm_button

    def set_layout(self, layout: QVBoxLayout):
        self._layout = layout

    def get_layout(self):
        return self._layout

    def add_data_source(self, data_source: MuseDataSource):
        self._data_sources.append(data_source)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    w = MuseDialog(QSize(800, 600), TupleEmitter())

    w.show()
    status = app.exec_()
    sys.exit(status)
