from PyQt5.QtCore import QSize, QRect, QDate
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QTableWidget, QPushButton, QHBoxLayout

from src.Emitters import TupleEmitter
from .MuseDialogWidget import MuseDialog
from ..MuseCalendarWidget import MuseCalendarWidget
from ..MuseComboBox import MuseComboBox
from ..MuseLabel import MuseLabel
from ..MuseLineEdit import MuseLineEdit
from ..MuseTableWidget import MuseTableWidget


class DialogFormFactory:

    def __init__(self, window_title: str,
                 button_label: str,
                 table_name: str,
                 row_data: list[tuple[str]],
                 table_part: MuseTableWidget = None):
        self.__window_title: str = window_title
        self.__button_label: str = button_label
        self.__table_name: str = table_name
        self.__row_data: list[tuple[str]] = row_data
        self.__table_part = table_part

    def __call__(self, parent_signal: TupleEmitter) -> MuseDialog:
        dialog_form = MuseDialog(QSize(800, 600), parent_signal)
        vertical_layout: QVBoxLayout = QVBoxLayout(dialog_form)
        dialog_form.setWindowTitle(self.__window_title)

        for header, attribute_type, data, possible_values in self.__row_data:
            vertical_layout.addWidget(MuseLabel(header, dialog_form))
            input_widget: QWidget
            match attribute_type:
                case MuseTableWidget.ItemType.enumType:
                    input_widget: MuseComboBox = MuseComboBox(QRect(10, 10, 100, 150), parent=dialog_form)
                    if data != "":
                        current_text_index = possible_values.index(data)
                        first_value = possible_values[0][:]
                        possible_values[0] = data
                        possible_values[current_text_index] = first_value
                    input_widget.addItems(possible_values)
                    pass

                case MuseTableWidget.ItemType.dateType:
                    input_widget: MuseCalendarWidget = MuseCalendarWidget(parent=dialog_form)
                    input_widget.setSelectedDate(QDate.fromString(data, "dd.MM.yyyy"))

                case _:
                    input_widget = MuseLineEdit(dialog_form)
                    input_widget.setText(data)
            vertical_layout.addWidget(input_widget)
            dialog_form.add_data_source(input_widget)

        dialog_form.get_confirm_button().setText(self.__button_label)
        dialog_form.set_layout(vertical_layout)
        dialog_form.setModal(True)

        if self.__table_part is None:
            vertical_layout.addWidget(dialog_form.get_confirm_button())
            return dialog_form

        vertical_layout.addWidget(dialog_form.get_confirm_button())
        return dialog_form
