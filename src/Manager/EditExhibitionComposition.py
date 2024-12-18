from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QHBoxLayout
from psycopg2.errors import RaiseException

from src.Emitters import TupleEmitter
from src.Handler import AlertMessageBox
from src.Manager.ManagerRepository import ManagerRepository
from src.SharedWidgets.MuseButton import MuseButton
from src.SharedWidgets.MuseDialog.MuseFindDialogWidget import MuseFindDialog
from src.SharedWidgets.MuseLabel import MuseLabel
from src.SharedWidgets.MuseTableWidget import MuseTableWidget


class EditExhibitionCompositionDialog(MuseFindDialog):

    def __init__(self, size: QSize,
                 exhibition_id: int,
                 attributes: dict[str, MuseTableWidget.ItemType],
                 parent_signal: TupleEmitter):
        MuseFindDialog.__init__(self, size=size, attributes=attributes, parent_signal=parent_signal)

        self._layout.removeWidget(self.get_confirm_button())
        self.__exhibition_id = exhibition_id

        self.__find_result_label = MuseLabel("Результаты поиска", self)
        self.__find_result_table = MuseTableWidget(attributes, self)
        self._layout.addWidget(self.__find_result_label)
        self._layout.addWidget(self.__find_result_table)
        self.__find_result_table.setHidden(True)
        self.__find_result_label.setHidden(True)

        self.__exhibition_composition_label = MuseLabel("Состав выставки", self)
        self.__exhibition_composition_table = MuseTableWidget(attributes, self)
        self._layout.addWidget(self.__exhibition_composition_label)
        self._layout.addWidget(self.__exhibition_composition_table)

        self.__actionsLayout = QHBoxLayout(self)
        self.__add_all_button = MuseButton("Добавить все", self)
        self.__add_all_button.setEnabled(False)
        self.__add_selected_button = MuseButton("Добавить", self)
        self.__remove_button = MuseButton("Убрать", self)
        self.__add_selected_button.setEnabled(False)
        self.__actionsLayout.addWidget(self._confirm_button)
        self.__actionsLayout.addWidget(self.__add_all_button)
        self.__actionsLayout.addWidget(self.__add_selected_button)
        self.__actionsLayout.addWidget(self.__remove_button)
        self._layout.addLayout(self.__actionsLayout)

        self.addFilterButton.clicked.connect(self.hide_exhibits_manipulations)
        self.removeFilterButton.clicked.connect(self.hide_exhibits_manipulations)
        self.__find_result_table.itemSelectionChanged.connect(lambda: self.__add_selected_button.setEnabled(True))
        self.update_exhibition_composition_table()

        self.__add_all_button.clicked.connect(self.add_all_to_exhibition)
        self.__add_selected_button.clicked.connect(self.add_exhibit_to_exhibition)
        self.__remove_button.clicked.connect(self.remove_exhibit_from_exhibition)

    def hide_exhibits_manipulations(self):
        self.__find_result_label.setHidden(True)
        self.__find_result_table.setHidden(True)
        self.__add_selected_button.setEnabled(False)
        self.__add_all_button.setEnabled(False)

    def _send_data(self):
        self.__find_result_table.setSortingEnabled(False)
        self.__find_result_table.setRowCount(0)
        self.__find_result_table.clear_ids()
        data_results = list(data_source.get_data() for data_source in self._data_sources)
        for i in range(len(data_results)):
            if self._attribute_types[self._active_filters[i]] != MuseTableWidget.ItemType.dateType:
                data_results[i] = f"like '%{data_results[i]}%'"
        data_results = [(self._active_filters[i].replace(" ", ""), data_results[i]) for i in range(len(data_results))]

        exhibits = ManagerRepository().find_available_exhibits(self.__exhibition_id, tuple(data_results))
        for exhibit in exhibits:
            self.__find_result_table.insertRow(self.__find_result_table.rowCount())
            self.__find_result_table.set_row(exhibit[1:])
            self.__find_result_table.add_id(int(exhibit[0]))

        self.__find_result_table.setSortingEnabled(True)
        self.__find_result_label.setHidden(False)
        self.__find_result_table.setHidden(False)
        self.__add_all_button.setEnabled(True)
        self.__add_selected_button.setEnabled(False)

    def update_exhibition_composition_table(self):
        self.__exhibition_composition_table.setSortingEnabled(False)
        self.__exhibition_composition_table.blockSignals(True)
        self.__exhibition_composition_table.setRowCount(0)
        self.__exhibition_composition_table.clear_ids()
        exhibits = ManagerRepository().get_exhibition_composition(self.__exhibition_id)
        for exhibit in exhibits:
            self.__exhibition_composition_table.insertRow(self.__exhibition_composition_table.rowCount())
            self.__exhibition_composition_table.set_row(exhibit[1:])
            self.__exhibition_composition_table.add_id(int(exhibit[0]))

        self.__exhibition_composition_table.setSortingEnabled(True)
        self.__exhibition_composition_table.blockSignals(False)
        if len(exhibits) == 0:
            self.__remove_button.setEnabled(False)

    def add_all_to_exhibition(self):
        ManagerRepository().add_exhibits_to_exhibitions(self.__exhibition_id, self.__find_result_table.get_ids())

        self.update_exhibition_composition_table()
        self._send_data()
        self.__remove_button.setEnabled(True)

    def add_exhibit_to_exhibition(self):
        ManagerRepository().add_exhibit_to_exhibition(self.__exhibition_id, self.__find_result_table.get_id(
            self.__find_result_table.currentRow()))

        self._send_data()
        self.update_exhibition_composition_table()
        self.__remove_button.setEnabled(True)

    def remove_exhibit_from_exhibition(self):
        ManagerRepository().remove_exhibit_from_exhibition(self.__exhibition_id,
                                                           self.__exhibition_composition_table.get_id(
                                                               self.__exhibition_composition_table.currentRow()))
        self._send_data()
        self.update_exhibition_composition_table()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    formDialogWindow = EditExhibitionCompositionDialog(QSize(1000, 800), 1,
                                                       {"Наименование": MuseTableWidget.ItemType.varchar,
                                                        "Вид": MuseTableWidget.ItemType.enumType,
                                                        "Номер зала": MuseTableWidget.ItemType.enumType,
                                                        "Описание": MuseTableWidget.ItemType.varchar,
                                                        "Размер": MuseTableWidget.ItemType.varchar,
                                                        "Год создания": MuseTableWidget.ItemType.varchar,
                                                        "Происхождение": MuseTableWidget.ItemType.varchar},
                                                       TupleEmitter(None))
    formDialogWindow.show()
    sys.exit(app.exec_())
