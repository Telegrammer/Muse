from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout, QDialog

from src.Emitters import TupleEmitter
from src.SharedWidgets.MuseButton import MuseButton
from src.SharedWidgets.MuseLabel import MuseLabel
from src.SharedWidgets.MuseLineEdit import MuseLineEdit
from src.SharedWidgets.MuseDialog.DialogFormFactory import DialogFormFactory


class ActsWidgetView(object):

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

        self.acceptActButton = MuseButton("Завершить акт", form)
        self.actionsLayout.addWidget(self.acceptActButton)

        self.requestLayout.addLayout(self.actionsLayout)


class ActsWidget(QDialog, ActsWidgetView):

    def __init__(self,
                 request_id: int,
                 exhibit_attributes: list[list],
                 parent: QWidget = None,
                 parent_signal: TupleEmitter = TupleEmitter(None)):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setModal(True)

        self.__parent_signal = parent_signal
        self.__request_id = request_id
        self.acceptActButton.clicked.connect(self.start_exhibit_insertion)
        self.__exhibit_attributes = exhibit_attributes

    def start_exhibit_insertion(self):

        exhibit_factory = DialogFormFactory("Добавить экспонат", 'Добавить', 'Экспонат', self.__exhibit_attributes)
        receive_signal = TupleEmitter(None)
        receive_signal.signal.connect(self.update_status)
        dialog_form = exhibit_factory(receive_signal)
        dialog_form.setModal(True)
        dialog_form.show()
        dialog_form.exec_()

    def update_status(self, dialog_output: tuple):
        self.__parent_signal.signal.emit((self.__request_id, 'закрыта', dialog_output))
        self.close()



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = ActsWidget(None, [["Название", 0, "Да", []]])
    Dialog.show()
    sys.exit(app.exec_())
