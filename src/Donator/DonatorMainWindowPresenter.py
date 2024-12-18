from typing import Callable

from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget, QShortcut

from src.Donator.DonatorFormDialog import DonatorFormDialog
from src.Donator.DonatorRepository import DonatorRepository
from src.Emitters import TupleEmitter
from src.Emitters import VoidEmitter
from src.SharedWidgets.Profile.DonatorProfile import DonatorProfilePresenter
from .DonatorWindowView import DonatorMainWindowView
from src.SharedWidgets.Statistic.StatisticWidget import StatisticWidget


class DonatorMainWindow(DonatorMainWindowView, QMainWindow):

    def __init__(self, parent_signal: VoidEmitter, user_data: tuple):
        QWidget.__init__(self, None)
        self.__user_data = user_data
        self.setupUi(self)
        self.update_tables()

        self.update_shortcut = QShortcut(QKeySequence("f5"), self)
        self.update_shortcut.activated.connect(self.update_tables)

        self.formActButton.clicked.connect(
            lambda: self.form_act_dialog(operation=self.add_request)
        )
        self.__quit_session_signal = parent_signal
        self.quitSessionAction_2.triggered.connect(
            lambda: self.__quit_session_signal.signal.emit()
        )
        self.quitSessionAction.triggered.connect(
            lambda: self.__quit_session_signal.signal.emit()
        )
        self.showpProfileInfoAction.triggered.connect(self.open_profile)
        self.showStatisticButton.clicked.connect(self.show_statistics)

    def show_statistics(self):
        exhibits = [(exhibit[-2], exhibit[-1]) for exhibit in
                    DonatorRepository().get_donator_popular_exhibits(self.__user_data[0])]
        statistics_window = StatisticWidget(exhibits)
        statistics_window.show()
        statistics_window.exec_()

    def open_profile(self):
        profile_window = DonatorProfilePresenter(self.__user_data, self)
        profile_window.setModal(True)
        profile_window.show()
        profile_window.exec_()

    def update_tables(self):
        self.update_exhibit_table()
        self.update_acts_table()

    def update_exhibit_table(self):
        self.exhibitTable.blockSignals(True)
        self.exhibitTable.setRowCount(0)
        self.exhibitTable.clear_ids()
        exhibits = DonatorRepository().get_donator_exhibits(self.__user_data[0])
        if exhibits is None:
            return
        for exhibit in exhibits:
            self.exhibitTable.insertRow(self.exhibitTable.rowCount())
            self.exhibitTable.set_row(exhibit[:])
        self.exhibitTable.blockSignals(False)

    def update_acts_table(self):
        self.actsTable.blockSignals(True)
        self.actsTable.setRowCount(0)
        self.actsTable.clear_ids()
        acts = DonatorRepository().get_donator_requests(self.__user_data[0])
        for act in acts:
            self.actsTable.insertRow(self.actsTable.rowCount())
            self.actsTable.add_id(act[0])
            self.actsTable.set_row(act[1:])
        self.actsTable.blockSignals(False)

    def form_act_dialog(self,
                        operation: Callable,
                        ):
        send_data_signal = TupleEmitter(self)
        send_data_signal.signal.connect(operation)
        dialog_form = DonatorFormDialog(send_data_signal)
        dialog_form.show()
        dialog_form.exec_()

    def add_request(self, dialog_output: tuple):
        DonatorRepository().add_request(self.__user_data[0], dialog_output[0])
        self.update_acts_table()
