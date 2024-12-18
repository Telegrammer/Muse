# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CuratorWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from src.SharedWidgets.MuseTableWidget import MuseTableWidget
from src.SharedWidgets.MuseButton import MuseButton

class CuratorMainWindowView(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1005, 679)
        MainWindow.setStyleSheet("QMenuBar {\n"
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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.donationActsLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.donationActsLabel.sizePolicy().hasHeightForWidth())
        self.donationActsLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.donationActsLabel.setFont(font)
        self.donationActsLabel.setStyleSheet("QLabel {\n"
                                             "    font: 87 12pt \"Arial Black\";\n"
                                             "    color: rgb(82, 30, 1);\n"
                                             "}")
        self.donationActsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.donationActsLabel.setObjectName("donationActsLabel")
        self.horizontalLayout_4.addWidget(self.donationActsLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.setVisibleDonationActsButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setVisibleDonationActsButton.sizePolicy().hasHeightForWidth())
        self.setVisibleDonationActsButton.setSizePolicy(sizePolicy)
        self.setVisibleDonationActsButton.setStyleSheet("\n"
                                                        "\n"
                                                        "QWidget {\n"
                                                        "    border 1px solid;\n"
                                                        "    border-radius: 20px;\n"
                                                        "    background-color: transparent;\n"
                                                        "    \n"
                                                        "}\n"
                                                        "\n"
                                                        "QPushButton {\n"
                                                        "    border-radius: 20px;\n"
                                                        "    border-style: outset;\n"
                                                        "\n"
                                                        "}\n"
                                                        "\n"
                                                        "QPushButton:hover {\n"
                                                        "    background: qradialgradient(\n"
                                                        "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                                        "        radius: 1.35, stop: 0.7 #faea99, stop: 1 #521e01\n"
                                                        "        );\n"
                                                        "    }\n"
                                                        "\n"
                                                        "QPushButton:pressed {\n"
                                                        "    border-style: inset;\n"
                                                        "    background: qradialgradient(\n"
                                                        "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                                        "        radius: 1.35, stop: 0 #fff, stop: 1 #521e01\n"
                                                        "        );\n"
                                                        "    }")
        self.setVisibleDonationActsButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("components/inactive drop button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setVisibleDonationActsButton.setIcon(icon)
        self.setVisibleDonationActsButton.setIconSize(QtCore.QSize(40, 40))
        self.setVisibleDonationActsButton.setObjectName("setVisibleDonationActsButton")
        self.horizontalLayout_4.addWidget(self.setVisibleDonationActsButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.tablesForDonationActsView = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tablesForDonationActsView.sizePolicy().hasHeightForWidth())
        self.tablesForDonationActsView.setSizePolicy(sizePolicy)
        self.tablesForDonationActsView.setObjectName("tablesForDonationActsView")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tablesForDonationActsView)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.actsTable = MuseTableWidget({"Даритель": MuseTableWidget.ItemType.enumType,
                                          "Электронная почта": MuseTableWidget.ItemType.varchar,
                                          "Дата передачи": MuseTableWidget.ItemType.dateType}, self.tablesForDonationActsView)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        self.actsTable.setSizePolicy(sizePolicy)
        self.actsTable.setMinimumSize(QtCore.QSize(330, 600))
        self.horizontalLayout.addWidget(self.actsTable)
        self.exhibitTable = MuseTableWidget({"Наименование": MuseTableWidget.ItemType.varchar,
                                             "Вид": MuseTableWidget.ItemType.varchar,
                                             "Номер зала": MuseTableWidget.ItemType.varchar,
                                             "Описание": MuseTableWidget.ItemType.varchar,
                                             "Размер": MuseTableWidget.ItemType.varchar,
                                             "Год создания": MuseTableWidget.ItemType.varchar,
                                             "Происхождение": MuseTableWidget.ItemType.varchar,
                                             }, parent=self.tablesForDonationActsView)
        self.exhibitTable.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.exhibitTable.setSizePolicy(sizePolicy)
        self.horizontalLayout.addWidget(self.exhibitTable)
        self.verticalLayout.addWidget(self.tablesForDonationActsView)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.viewDonationActsWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewDonationActsWidget.sizePolicy().hasHeightForWidth())
        self.viewDonationActsWidget.setSizePolicy(sizePolicy)
        self.viewDonationActsWidget.setMinimumSize(QtCore.QSize(250, 51))
        self.viewDonationActsWidget.setObjectName("viewDonationActsWidget")
        self.viewRequestsForDonationButton = QtWidgets.QPushButton(self.viewDonationActsWidget)
        self.viewRequestsForDonationButton.setGeometry(QtCore.QRect(10, 10, 220, 31))
        self.viewRequestsForDonationButton.setMinimumSize(QtCore.QSize(220, 31))
        self.viewRequestsForDonationButton.setMaximumSize(QtCore.QSize(16777215, 31))
        self.viewRequestsForDonationButton.setStyleSheet("QWidget {\n"
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
        self.viewRequestsForDonationButton.setObjectName("viewRequestsForDonationButton")
        self.uncheckedRequestsLabel = QtWidgets.QLabel(self.viewDonationActsWidget)
        self.uncheckedRequestsLabel.setGeometry(QtCore.QRect(220, 0, 21, 21))
        self.uncheckedRequestsLabel.setStyleSheet("\n"
                                                  "\n"
                                                  "QWidget {\n"
                                                  "background-color: rgb(255, 0, 4);\n"
                                                  "    font: 87 8pt \"Arial Black\";\n"
                                                  "    \n"
                                                  "    border: 2px rgb(255, 0, 4);\n"
                                                  "    border-radius: 10px;\n"
                                                  "    color: rgb(255, 255, 255);\n"
                                                  "\n"
                                                  "}")
        self.uncheckedRequestsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.uncheckedRequestsLabel.setObjectName("uncheckedRequestsLabel")
        self.horizontalLayout_2.addWidget(self.viewDonationActsWidget)

        self.viewApprovedRequestsWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewApprovedRequestsWidget.sizePolicy().hasHeightForWidth())
        self.viewApprovedRequestsWidget.setSizePolicy(sizePolicy)
        self.viewApprovedRequestsWidget.setMinimumSize(QtCore.QSize(231, 51))
        self.viewApprovedRequestsWidget.setObjectName("viewDonationActsWidget")
        self.viewRequestsForActButton = QtWidgets.QPushButton(self.viewApprovedRequestsWidget)
        self.viewRequestsForActButton.setText("Открыть одобренные заявки")
        self.viewRequestsForActButton.setGeometry(QtCore.QRect(10, 10, 201, 31))
        self.viewRequestsForActButton.setMinimumSize(QtCore.QSize(100, 31))
        self.viewRequestsForActButton.setMaximumSize(QtCore.QSize(16777215, 31))
        self.viewRequestsForActButton.setStyleSheet("QWidget {\n"
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
        self.viewRequestsForActButton.setObjectName("viewRequestsForDonationButton")
        self.approvedRequestsLabel = QtWidgets.QLabel(self.viewApprovedRequestsWidget)
        self.approvedRequestsLabel.setGeometry(QtCore.QRect(200, 0, 21, 21))
        self.approvedRequestsLabel.setStyleSheet("\n"
                                                  "\n"
                                                  "QWidget {\n"
                                                  "background-color: rgb(255, 0, 4);\n"
                                                  "    font: 87 8pt \"Arial Black\";\n"
                                                  "    \n"
                                                  "    border: 2px rgb(255, 0, 4);\n"
                                                  "    border-radius: 10px;\n"
                                                  "    color: rgb(255, 255, 255);\n"
                                                  "\n"
                                                  "}")
        self.approvedRequestsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.approvedRequestsLabel.setObjectName("uncheckedRequestsLabel")

        self.horizontalLayout_2.addWidget(self.viewApprovedRequestsWidget)
        self.findActsButton = MuseButton('Поиск', MainWindow)
        self.horizontalLayout_2.addWidget(self.findActsButton)

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1005, 21))
        self.menubar.setObjectName("menubar")
        self.profileMenu = QtWidgets.QMenu(self.menubar)
        self.profileMenu.setObjectName("profileMenu")
        self.RequestsMenu = QtWidgets.QMenu(self.menubar)
        self.RequestsMenu.setObjectName("RequestsMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.showProfileAction = QtWidgets.QAction(MainWindow)
        self.showProfileAction.setObjectName("showProfileAction")
        self.quitSessionAction = QtWidgets.QAction(MainWindow)
        self.quitSessionAction.setObjectName("quitSessionAction")
        self.openRequestsListAction = QtWidgets.QAction(MainWindow)
        self.openRequestsListAction.setEnabled(True)
        self.openRequestsListAction.setObjectName("openRequestsListAction")
        self.closeRequestListAction = QtWidgets.QAction(MainWindow)
        self.closeRequestListAction.setObjectName("closeRequestListAction")
        self.profileMenu.addAction(self.showProfileAction)
        self.profileMenu.addSeparator()
        self.profileMenu.addAction(self.quitSessionAction)
        self.RequestsMenu.addAction(self.openRequestsListAction)
        self.menubar.addAction(self.profileMenu.menuAction())
        self.menubar.addAction(self.RequestsMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.donationActsLabel.setText(_translate("MainWindow", "Акты дарения"))
        # self.actsTable.setSortingEnabled(True)
        self.exhibitTable.setSortingEnabled(True)
        self.viewRequestsForDonationButton.setText(_translate("MainWindow", "Открыть необработанные запросы"))
        self.uncheckedRequestsLabel.setText(_translate("MainWindow", "99+"))
        self.profileMenu.setTitle(_translate("MainWindow", "Профиль"))
        self.RequestsMenu.setTitle(_translate("MainWindow", "Запросы"))
        self.showProfileAction.setText(_translate("MainWindow", "Показать"))
        self.quitSessionAction.setText(_translate("MainWindow", "Выход"))
        self.quitSessionAction.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.openRequestsListAction.setText(_translate("MainWindow", "Открыть"))
        self.closeRequestListAction.setText(_translate("MainWindow", "Закрыть"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = CuratorMainWindowView()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
