from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout, QDialog

from src.Emitters import TupleEmitter
from src.SharedWidgets.MuseButton import MuseButton
from src.SharedWidgets.MuseLabel import MuseLabel
from src.SharedWidgets.MuseLineEdit import MuseLineEdit


class RequestWidgetView(object):

    def setupUi(self, form: QWidget = None):
        form.setStyleSheet("QMenuBar {\n"
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
        self.requestLayout = QVBoxLayout(form)
        form.setLayout(self.requestLayout)
        self.headerInfoLayout = QHBoxLayout(form)

        self.donatorLayout = QVBoxLayout(form)
        self.donatorLayout.addWidget(MuseLabel("Даритель", form))
        self.donatorLineEdit = MuseLineEdit(form)
        self.donatorLineEdit.setReadOnly(True)
        self.donatorLayout.addWidget(self.donatorLineEdit)
        self.headerInfoLayout.addLayout(self.donatorLayout)

        self.formDateLayout = QVBoxLayout(form)
        self.formDateLayout.addWidget(MuseLabel("Дата оформления", form))
        self.formDateLineEdit = MuseLineEdit(form)
        self.formDateLineEdit.setReadOnly(True)
        self.formDateLayout.addWidget(self.formDateLineEdit)
        self.headerInfoLayout.addLayout(self.formDateLayout)

        self.requestLayout.addLayout(self.headerInfoLayout)

        self.descriptionLineEdit = MuseLineEdit(form)
        self.requestLayout.addWidget(self.descriptionLineEdit)

        self.actionsLayout = QHBoxLayout(form)

        self.acceptRequestButton = MuseButton("Одобрить проведение передачи", form)
        self.actionsLayout.addWidget(self.acceptRequestButton)

        self.rejectRequestButton = MuseButton("Отказать", form)
        self.actionsLayout.addWidget(self.rejectRequestButton)

        self.requestLayout.addLayout(self.actionsLayout)


class RequestWidget(QDialog, RequestWidgetView):

    def __init__(self,
                 request_id: int,
                 parent: QWidget = None,
                 parent_signal: TupleEmitter = TupleEmitter(None)):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setModal(True)

        self.__parent_signal = parent_signal
        self.__request_id = request_id
        self.acceptRequestButton.clicked.connect(lambda: self.send_status('одобрена'))
        self.rejectRequestButton.clicked.connect(lambda: self.send_status('отказано'))

    def send_status(self, status: str):
        self.__parent_signal.signal.emit((self.__request_id, status))
        self.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = RequestWidget(None)
    Dialog.show()
    sys.exit(app.exec_())
