from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QVBoxLayout

from src.Emitters import TupleEmitter
from src.SharedWidgets import MuseDialog, MuseLabel, MuseLineEdit


class DialogFormFactory:

    def __init__(self, window_title: str,
                 button_label: str,
                 table_name: str,
                 row_data: list[tuple[str]]):
        self.__window_title: str = window_title
        self.__button_label: str = button_label
        self.__table_name: str = table_name
        self.__row_data: list[tuple[str]] = row_data

    def __call__(self, parent_signal: TupleEmitter) -> MuseDialog:
        dialog_form = MuseDialog(QSize(800, 600), parent_signal)
        vertical_layout = QVBoxLayout(dialog_form)
        dialog_form.setWindowTitle(self.__window_title)

        for header, data in self.__row_data:
            vertical_layout.addWidget(MuseLabel(header, dialog_form))
            line_edit = MuseLineEdit(dialog_form)
            line_edit.setText(data)
            vertical_layout.addWidget(line_edit)
            dialog_form.add_data_source(line_edit)

        dialog_form.get_confirm_button().setText(self.__button_label)
        vertical_layout.addWidget(dialog_form.get_confirm_button())

        dialog_form.setModal(True)
        return dialog_form
