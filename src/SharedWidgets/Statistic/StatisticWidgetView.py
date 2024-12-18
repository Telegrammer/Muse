# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statisticwidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from PyQt5 import QtCore, QtWidgets
from src.SharedWidgets.MuseLabel import MuseLabel

class StatisticWidgetView(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 600)
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
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleLabel = MuseLabel("10 Самых популярных экспонатов", Form)
        self.verticalLayout.addWidget(self.titleLabel)
        self.diagramFrame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.diagramFrame.sizePolicy().hasHeightForWidth())
        self.diagramFrame.setSizePolicy(sizePolicy)
        self.diagramFrame.setStyleSheet("background-color: #fff2c6;\n"
                                        "border: 1px solid;\n"
                                        "border-radius: 15px;\n"
                                        "")
        self.diagramFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.diagramFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.diagramFrame.setObjectName("diagramFrame")
        self.horizontal_layout = QtWidgets.QHBoxLayout(self.diagramFrame)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)


        self.horizontal_layout.addWidget(self.canvas)
        self.verticalLayout.addWidget(self.diagramFrame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Статистика"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = StatisticWidgetView()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
