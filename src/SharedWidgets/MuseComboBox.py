# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets

from src.SharedWidgets.MuseDataSource import MuseDataSource, StringEmitter


class MuseComboBoxView(object):

    def setup_ui(self, rect: QtCore.QRect, combo_box: QtWidgets.QComboBox):
        combo_box.setGeometry(rect)
        combo_box.setStyleSheet("QWidget {\n"
                                "    background-color: rgb(250, 234, 153);\n"
                                "    border: 1px solid rgb(250, 201, 131);\n"
                                "    border-radius: 10px;\n"
                                "    text-align: center;\n"
                                "}\n"
                                "\n"
                                "QComboBox {\n"
                                "    \n"
                                "    font: 87 8pt \"Arial Black\";\n"
                                "    color: rgb(82, 30, 1);\n"
                                "}\n"
                                "QComboBox:hover:!pressed {\n"
                                "  border: 2px solid rgb(250, 201, 131);\n"
                                "}")


class MuseComboBox(QtWidgets.QComboBox, MuseComboBoxView, MuseDataSource):
    def __init__(self, rect: QtCore.QRect, parent: QtCore.QObject = None,
                 parent_signal: StringEmitter = StringEmitter(None)):
        QtWidgets.QComboBox.__init__(self, parent)
        self.__parent_signal = parent_signal
        self.setup_ui(rect, self)

    def get_data(self):
        return self.currentText()

    def return_data_before_destroy(self):
        self.__parent_signal.signal.emit(self.get_data())

    def closeEvent(self, *args, **kwargs):
        self.return_data_before_destroy()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = MuseComboBox(QtCore.QRect(10, 10, 100, 100))
    Form.show()
    sys.exit(app.exec_())
