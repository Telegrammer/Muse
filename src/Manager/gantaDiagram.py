import datetime
from datetime import timedelta

from PyQt5 import QtCore, QtWidgets

from src.Manager.ManagerRepository import ManagerRepository
from src.SharedWidgets.MuseButton import MuseButton


class ExhibitionCalendarDiagramView(object):
    def setupUi(self, Form, exhibitions, month_width: int):
        Form.setObjectName("Form")
        Form.resize(1059, 664)
        Form.setStyleSheet("QMenuBar {\n"
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
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1042, 630))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gantaDiagramDataWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gantaDiagramDataWidget.sizePolicy().hasHeightForWidth())
        self.gantaDiagramDataWidget.setSizePolicy(sizePolicy)
        self.gantaDiagramDataWidget.setMinimumSize(QtCore.QSize(1024, 10000))
        self.gantaDiagramDataWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gantaDiagramDataWidget.setObjectName("gantaDiagramDataWidget")

        max_delta: timedelta = exhibitions[-1][-1] - exhibitions[0][2]
        window_width = max_delta.days * 3
        first_month: int = 0
        self.gantaDiagramDataWidget.setFixedWidth(window_width + month_width)

        current_line_pos = month_width
        while current_line_pos < window_width + 30:
            line = QtWidgets.QFrame(self.gantaDiagramDataWidget)
            line.setGeometry(QtCore.QRect(current_line_pos, 0, 2, 100000000))
            line.setFrameShape(QtWidgets.QFrame.VLine)
            line.setFrameShadow(QtWidgets.QFrame.Sunken)
            current_line_pos += month_width
            first_month %= 12
            if first_month == 0:
                line.setMinimumSize(QtCore.QSize(2, 0))
                line.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "border-color: rgb(125, 116, 255);\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "\n"
                                   "border: 2px solid;")
                first_month += 1

            first_month += 1

        start_date = datetime.date(exhibitions[0][2].year, exhibitions[0][2].month, 1)
        current_exhibition_pos_y = 30
        start_year_pos = 0
        btns = []
        for i in range(len(exhibitions)):
            label = MuseButton(str(i), self.gantaDiagramDataWidget)
            exhibition_delta = exhibitions[i][3] - exhibitions[i][2]
            year_delta = exhibitions[i][2].year - start_date.year
            start_year_pos = year_delta * month_width * 12 - (month_width * year_delta) + month_width
            year_start_date = datetime.date(exhibitions[i][2].year, 1, 1)
            month_delta = exhibitions[i][2].month - 1
            print(month_delta)
            start_month_pos = month_delta * month_width
            btn = MuseButton(str(i), self.gantaDiagramDataWidget)
            btn.setGeometry(QtCore.QRect(start_year_pos + start_month_pos, current_exhibition_pos_y, 100, 40))
            btn.setFixedHeight(30)
            current_exhibition_pos_y += 32
            btns.append(btn)

        self.verticalLayout.addWidget(self.gantaDiagramDataWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        QtCore.QMetaObject.connectSlotsByName(Form)


class ExhibitionCalendarDiagram(QtWidgets.QWidget, ExhibitionCalendarDiagramView):

    def __init__(self, parent: QtCore.QObject = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.__exhibitions = ManagerRepository().get_exhibition_calendar_info()
        self.__month_width = 60
        self.setupUi(self, self.__exhibitions, self.__month_width)

        self.__horizontal_scroll: QtWidgets.QScrollBar = self.scrollArea.horizontalScrollBar()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = ExhibitionCalendarDiagram()
    Form.show()
    sys.exit(app.exec_())
