from PyQt5.QtWidgets import QMainWindow, QScrollBar
from PyQt5.QtWidgets import QWidget

from src.Curator.CuratorRepository import CuratorRepository
from src.Curator.Requests.CuratorFormDialogFactory import CuratorFormDialogFactory
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
        self.viewRequestsForDonationButton.clicked.connect(self.open_requests)

        self.__quit_session_signal = parent_signal
        self.quitSessionAction.triggered.connect(
            lambda: self.__quit_session_signal.signal.emit()
        )

    def open_requests(self):

        dialog_form_factory = CuratorFormDialogFactory(CuratorRepository().find_unchecked_requests())
        dialog_form = dialog_form_factory()
        dialog_form.show()
        dialog_form.exec_()

    def update_request_status(self, request_id: int):
        pass

    def set_exhibit_table_scroll_bar(self):
        self.__exhibitsScrollBar.setValue(self.__actsScrollBar.value())

    def update_requests_count(self):
        count = CuratorRepository().count_unchecked_requests()
        if count > 99:
            self.uncheckedRequestsLabel.setText("99+")
        else:
            self.uncheckedRequestsLabel.setText(str(count))

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
