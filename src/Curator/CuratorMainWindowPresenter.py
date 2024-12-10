from typing import Callable

from PyQt5.QtWidgets import QMainWindow, QScrollBar
from PyQt5.QtWidgets import QWidget

from src.Curator.CuratorRepository import CuratorRepository
from src.Curator.Requests.CuratorFormDialogFactory import CuratorFormDialogFactory
from src.Emitters import TupleEmitter
from src.Emitters import VoidEmitter
from .CuratorWindowView import CuratorMainWindowView


class CuratorMainWindow(QMainWindow, CuratorMainWindowView):

    def __init__(self, parent_signal: VoidEmitter, user_data: tuple):
        QWidget.__init__(self, None)
        self.__user_data = user_data
        self.setupUi(self)
        self.__actsScrollBar: QScrollBar = self.actsTable.verticalScrollBar()
        self.__exhibitsScrollBar: QScrollBar = self.exhibitTable.verticalScrollBar()
        self.update_tables()
        self.__actsScrollBar.valueChanged.connect(self.set_exhibit_table_scroll_bar)
        self.viewRequestsForDonationButton.clicked.connect(
            lambda: self.open_requests('unchecked', self.update_request)
        )

        self.viewRequestsForActButton.clicked.connect(
            lambda: self.open_requests('approved', self.add_exhibit)
        )

        self.__quit_session_signal = parent_signal
        self.quitSessionAction.triggered.connect(
            lambda: self.__quit_session_signal.signal.emit()
        )

    def add_exhibit(self, dialog_output):
        exhibit_name, exhibit_type, hall, description, size, creation_year, origin = dialog_output[2]
        CuratorRepository().add_exhibit(exhibit_name,
                                        exhibit_type,
                                        hall,
                                        description,
                                        size,
                                        creation_year,
                                        origin)

        repository = CuratorRepository()
        repository.add_act(repository.get_donator_by_request_id(dialog_output[0]))
        self.update_request((dialog_output[0], dialog_output[1]))
        self.update_tables()

    def update_request(self, dialog_output):
        CuratorRepository().update_request_status(dialog_output[0], dialog_output[1])
        self.update_requests_count()

    def open_requests(self, mode: str, operation: Callable):
        data_for_factory_methods = {"approved": self.get_approved_requests(),
                                    "unchecked": self.get_unchecked_requests()}
        dialog_form_factory = CuratorFormDialogFactory(data_for_factory_methods[mode], mode)
        receive_signal = TupleEmitter(None)
        receive_signal.signal.connect(operation)
        dialog_form = dialog_form_factory(self.exhibitTable.get_row_data(is_new_row=True), receive_signal)
        dialog_form.show()
        dialog_form.exec_()

    @staticmethod
    def get_unchecked_requests():
        return CuratorRepository().find_unchecked_requests()

    @staticmethod
    def get_approved_requests():
        return CuratorRepository().find_approved_requests()

    def set_exhibit_table_scroll_bar(self):
        self.__exhibitsScrollBar.setValue(self.__actsScrollBar.value())

    def update_requests_count(self):
        unchecked_count = CuratorRepository().count_unchecked_requests()
        approved_count = CuratorRepository().count_approved_requests()
        self.uncheckedRequestsLabel.setHidden(False)
        if unchecked_count > 99:
            self.uncheckedRequestsLabel.setText("99+")
        else:
            self.uncheckedRequestsLabel.setText(str(unchecked_count))
        if approved_count > 99:
            self.approvedRequestsLabel.setText("99+")
        else:
            self.approvedRequestsLabel.setText(str(approved_count))

        if unchecked_count == 0:
            self.uncheckedRequestsLabel.setHidden(True)

        if approved_count == 0:
            self.approvedRequestsLabel.setHidden(True)

    def update_tables(self):
        self.update_requests_count()
        self.exhibitTable.blockSignals(True)
        self.actsTable.blockSignals(True)
        self.exhibitTable.setRowCount(0)
        self.actsTable.setRowCount(0)
        donation_acts = CuratorRepository().get_donation_acts()
        for act in donation_acts:
            self.actsTable.insertRow(self.actsTable.rowCount())
            self.actsTable.set_row(act[:3])
            self.exhibitTable.insertRow(self.exhibitTable.rowCount())
            self.exhibitTable.set_row(act[3:])
        self.exhibitTable.set_attribute_values("Вид", CuratorRepository().get_exhibit_types())
        self.exhibitTable.set_attribute_values("Номер зала", CuratorRepository().get_exhibit_halls())
        self.exhibitTable.blockSignals(False)
        self.actsTable.blockSignals(False)
        self.__actsScrollBar.setSliderPosition(self.__actsScrollBar.maximum())
