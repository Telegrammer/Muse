from PyQt5.QtCore import QObject, QDate
from PyQt5.QtWidgets import QCalendarWidget, QSizePolicy

from src.SharedWidgets.MuseDataSource import MuseDataSource, StringEmitter


class MuseCalendarWidgetView(object):

    def setup_ui(self, calendar: QCalendarWidget):
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(calendar.sizePolicy().hasHeightForWidth())
        calendar.setSizePolicy(sizePolicy)
        calendar.setStyleSheet("QCalendarWidget QWidget{\n"
                               "    \n"
                               "    font: 87 8pt \"Arial Black\";\n"
                               "    color: #521e01;\n"
                               "    background-color: #faebb4;\n"
                               "}\n"
                               "\n"
                               "\n"
                               "QCalendarWidget QAbstractItemView:enabled{\n"
                               "background-color: #fffddf;\n"
                               "font: 75 8pt \"Arial\";\n"
                               "color: black;\n"
                               "}")


class MuseCalendarWidget(QCalendarWidget, MuseDataSource, MuseCalendarWidgetView):

    def __init__(self, parent: QObject = None, parent_signal: StringEmitter = StringEmitter(None)):
        QCalendarWidget.__init__(self, parent)
        self.setup_ui(self)
        self.__parent_signal = parent_signal

    def get_data(self):
        selected_date: QDate = self.selectedDate()
        return selected_date.toString("dd.MM.yyyy")

    def return_data_before_destroy(self):
        self.__parent_signal.signal.emit(self.get_data())
