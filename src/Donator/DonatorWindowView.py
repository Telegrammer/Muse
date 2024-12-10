# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DonatorWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets

from src.SharedWidgets import MuseTableWidget


class DonatorMainWindowView(object):
    def setupUi(self, ManagerMainWindow):
        ManagerMainWindow.setObjectName("ManagerMainWindow")
        ManagerMainWindow.resize(931, 791)
        ManagerMainWindow.setStyleSheet("QMenuBar {\n"
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
        self.centralwidget = QtWidgets.QWidget(ManagerMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tablesForDonationActsView = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tablesForDonationActsView.sizePolicy().hasHeightForWidth())
        self.tablesForDonationActsView.setSizePolicy(sizePolicy)
        self.tablesForDonationActsView.setObjectName("tablesForDonationActsView")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tablesForDonationActsView)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.actsTable = MuseTableWidget({'Описание': MuseTableWidget.ItemType.varchar,
                                          'Дата формирования': MuseTableWidget.ItemType.dateType,
                                          'Статус': MuseTableWidget.ItemType.enumType}, self.tablesForDonationActsView)
        self.actsTable.setEnabled(True)
        self.horizontalLayout.addWidget(self.actsTable)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formActButton = QtWidgets.QPushButton(self.tablesForDonationActsView)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formActButton.sizePolicy().hasHeightForWidth())
        self.formActButton.setSizePolicy(sizePolicy)
        self.formActButton.setMinimumSize(QtCore.QSize(200, 31))
        self.formActButton.setMaximumSize(QtCore.QSize(16777215, 31))
        self.formActButton.setStyleSheet("QWidget {\n"
                                         "    background-color: rgb(250, 234, 153);\n"
                                         "    border: 1px solid rgb(250, 201, 131);\n"
                                         "    border-radius: 10px;\n"
                                         "    text-align: center;\n"
                                         "}\n"
                                         "\n"
                                         "QAbstractButton {\n"
                                         "    \n"
                                         "    font: 87 8pt \"Arial Black\";\n"
                                         "    color: rgb(82, 30, 1);\n"
                                         "}\n"
                                         "QPushButton:hover:!pressed {\n"
                                         "  border: 2px solid rgb(250, 201, 131);\n"
                                         "}")
        self.formActButton.setObjectName("formActButton")
        self.verticalLayout_2.addWidget(self.formActButton)
        self.showStatisticButton = QtWidgets.QPushButton(self.tablesForDonationActsView)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showStatisticButton.sizePolicy().hasHeightForWidth())
        self.showStatisticButton.setSizePolicy(sizePolicy)
        self.showStatisticButton.setMinimumSize(QtCore.QSize(200, 31))
        self.showStatisticButton.setMaximumSize(QtCore.QSize(16777215, 31))
        self.showStatisticButton.setStyleSheet("QWidget {\n"
                                               "    background-color: rgb(250, 234, 153);\n"
                                               "    border: 1px solid rgb(250, 201, 131);\n"
                                               "    border-radius: 10px;\n"
                                               "    text-align: center;\n"
                                               "}\n"
                                               "\n"
                                               "QAbstractButton {\n"
                                               "    \n"
                                               "    font: 87 8pt \"Arial Black\";\n"
                                               "    color: rgb(82, 30, 1);\n"
                                               "}\n"
                                               "QPushButton:hover:!pressed {\n"
                                               "  border: 2px solid rgb(250, 201, 131);\n"
                                               "}")
        self.showStatisticButton.setObjectName("showStatisticButton")
        self.verticalLayout_2.addWidget(self.showStatisticButton)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addWidget(self.tablesForDonationActsView)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("QLabel {\n"
                                 "    font: 87 12pt \"Arial Black\";\n"
                                 "    color: rgb(82, 30, 1);\n"
                                 "}")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.exhibitWidget = QtWidgets.QWidget(self.centralwidget)
        self.exhibitWidget.setMinimumSize(QtCore.QSize(0, 300))
        self.exhibitWidget.setObjectName("exhibitWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.exhibitWidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3.addWidget(self.exhibitWidget)
        ManagerMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ManagerMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 931, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        ManagerMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ManagerMainWindow)
        self.statusbar.setObjectName("statusbar")
        ManagerMainWindow.setStatusBar(self.statusbar)
        self.selectEmployeeTableAction = QtWidgets.QAction(ManagerMainWindow)
        self.selectEmployeeTableAction.setCheckable(True)
        self.selectEmployeeTableAction.setChecked(True)
        self.selectEmployeeTableAction.setObjectName("selectEmployeeTableAction")
        self.action = QtWidgets.QAction(ManagerMainWindow)
        self.action.setObjectName("action")
        self.viewProfileInfoAction = QtWidgets.QAction(ManagerMainWindow)
        self.viewProfileInfoAction.setObjectName("viewProfileInfoAction")
        self.quitSessionAction = QtWidgets.QAction(ManagerMainWindow)
        self.quitSessionAction.setObjectName("quitSessionAction")
        self.showpProfileInfoAction = QtWidgets.QAction(ManagerMainWindow)
        self.showpProfileInfoAction.setObjectName("showpProfileInfoAction")
        self.quitSessionAction_2 = QtWidgets.QAction(ManagerMainWindow)
        self.quitSessionAction_2.setObjectName("quitSessionAction_2")
        self.menu.addAction(self.showpProfileInfoAction)
        self.menu.addSeparator()
        self.menu.addAction(self.quitSessionAction_2)
        self.menubar.addAction(self.menu.menuAction())

        self.exhibitTable = MuseTableWidget({"Наименование": MuseTableWidget.ItemType.varchar,
                                             "Вид": MuseTableWidget.ItemType.enumType,
                                             "Описание": MuseTableWidget.ItemType.varchar,
                                             "Размер": MuseTableWidget.ItemType.varchar,
                                             "Год создания": MuseTableWidget.ItemType.integer,
                                             "Происхождение": MuseTableWidget.ItemType.varchar,
                                             }, parent=self.exhibitWidget)
        self.verticalLayout_4.addWidget(self.exhibitTable)

        self.retranslateUi(ManagerMainWindow)
        QtCore.QMetaObject.connectSlotsByName(ManagerMainWindow)

    def retranslateUi(self, ManagerMainWindow):
        _translate = QtCore.QCoreApplication.translate
        ManagerMainWindow.setWindowTitle(_translate("ManagerMainWindow", "Главное окно - (Даритель)"))
        self.formActButton.setText(_translate("ManagerMainWindow", "Сформировать акт"))
        self.formActButton.setShortcut(_translate("ManagerMainWindow", "Ctrl+S"))
        self.showStatisticButton.setText(_translate("ManagerMainWindow", "Посмотреть статистику"))
        self.showStatisticButton.setShortcut(_translate("ManagerMainWindow", "Ctrl+S"))
        self.label.setText(_translate("ManagerMainWindow", "Ваши экспонаты"))
        self.menu.setTitle(_translate("ManagerMainWindow", "Профиль"))
        self.selectEmployeeTableAction.setText(_translate("ManagerMainWindow", "Выбрать"))
        self.action.setText(_translate("ManagerMainWindow", "Поиск..."))
        self.viewProfileInfoAction.setText(_translate("ManagerMainWindow", "Показать"))
        self.quitSessionAction.setText(_translate("ManagerMainWindow", "Выход"))
        self.showpProfileInfoAction.setText(_translate("ManagerMainWindow", "Показать"))
        self.quitSessionAction_2.setText(_translate("ManagerMainWindow", "Выход"))
        self.quitSessionAction_2.setShortcut(_translate("ManagerMainWindow", "Ctrl+Q"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ManagerMainWindow = QtWidgets.QMainWindow()
    ui = Ui_ManagerMainWindow()
    ui.setupUi(ManagerMainWindow)
    ManagerMainWindow.show()
    sys.exit(app.exec_())
