from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QVBoxLayout, QScrollArea, QWidget

from src.Curator.Requests.RequestWidget import RequestWidget
from src.Emitters import TupleEmitter
from src.SharedWidgets.MuseDialog.MuseFindDialogWidget import MuseDialog
from src.SharedWidgets.MuseButton import MuseButton

class CuratorRequestsDialog(MuseDialog):

    def __init__(self, parent_signal: TupleEmitter = TupleEmitter(None)):
        MuseDialog.__init__(self, QSize(600, 700), parent_signal)
        self.setWindowTitle('Заявки дарителей')
        self.set_layout(QVBoxLayout(None))
        self._data_transfer = parent_signal

        self.__scrollArea = QScrollArea(self)
        self.requests = QWidget()
        self.__requestsLayout = QVBoxLayout(self.requests)
        self.requests.setLayout(self.__requestsLayout)
        self.__scrollArea.setWidget(self.requests)

        self._layout.addWidget(self.__scrollArea)

        self._layout.addWidget(self.get_confirm_button())
        self.__requestsLayout.addWidget(MuseButton('', self.requests))
        self._confirm_button.setText("Закрыть")
        self.setLayout(self._layout)

    def add_request_widget(self, widget: RequestWidget):
        widget.setParent(self.requests)
        self.__requestsLayout.addWidget(widget)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = CuratorRequestsDialog()
    Dialog.show()
    sys.exit(app.exec_())
