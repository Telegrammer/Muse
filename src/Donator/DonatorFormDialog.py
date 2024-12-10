from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QVBoxLayout

from src.Emitters import TupleEmitter
from src.SharedWidgets.MuseDialog.MuseFindDialogWidget import MuseDialog
from src.SharedWidgets.MuseLabel import MuseLabel
from src.SharedWidgets.MuseLineEdit import MuseLineEdit


class DonatorFormDialog(MuseDialog):

    def __init__(self, parent_signal: TupleEmitter = TupleEmitter(None)):
        MuseDialog.__init__(self, QSize(400, 300), parent_signal)
        self.setWindowTitle('Начать формировку акта')
        self._layout = QVBoxLayout(self)
        self._layout.addWidget(MuseLabel('Описание экспоната', self))
        data_source = MuseLineEdit(self)
        self.add_data_source(data_source)
        self._layout.addWidget(data_source)
        self._layout.addWidget(self.get_confirm_button())
        self.get_confirm_button().setText("Оставить заявку")
        self.setLayout(self._layout)