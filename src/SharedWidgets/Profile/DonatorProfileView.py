


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Profile.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from src.SharedWidgets.MuseLineEdit import MuseLineEdit


class ProfileWindowView(object):
    def setupUi(self, profileDialog):
        profileDialog.setObjectName("profileDialog")
        profileDialog.setWindowModality(QtCore.Qt.WindowModal)
        profileDialog.resize(599, 510)
        profileDialog.setStyleSheet("QMenuBar {\n"
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
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(profileDialog)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.employeeLabel = QtWidgets.QLabel(profileDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.employeeLabel.sizePolicy().hasHeightForWidth())
        self.employeeLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.employeeLabel.setFont(font)
        self.employeeLabel.setStyleSheet("QLabel {\n"
                                         "    font: 87 12pt \"Arial Black\";\n"
                                         "    color: rgb(82, 30, 1);\n"
                                         "}")
        self.employeeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.employeeLabel.setObjectName("employeeLabel")
        self.verticalLayout_6.addWidget(self.employeeLabel)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.fullnameLabel = QtWidgets.QLabel(profileDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fullnameLabel.sizePolicy().hasHeightForWidth())
        self.fullnameLabel.setSizePolicy(sizePolicy)
        self.fullnameLabel.setStyleSheet("QLabel {\n"
                                         "    font: 87 8pt \"Arial Black\";\n"
                                         "    color: rgb(82, 30, 1);\n"
                                         "}")
        self.fullnameLabel.setObjectName("fullnameLabel")
        self.verticalLayout.addWidget(self.fullnameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(profileDialog)
        self.nameLineEdit.setMinimumSize(QtCore.QSize(0, 31))
        self.nameLineEdit.setMaximumSize(QtCore.QSize(16777215, 31))
        self.nameLineEdit.setStyleSheet("QLineEdit {\n"
                                        "    \n"
                                        "    font: 8pt \"Arial\";\n"
                                        "    padding-left: 10px;\n"
                                        "    padding-right: 10px;\n"
                                        "    background-color: rgb(250, 235, 180);\n"
                                        "    border-radius: 10px;\n"
                                        "}\n"
                                        "\n"
                                        "QLineEdit:focus {\n"
                                        "  border: 2px solid rgb(250, 201, 131);\n"
                                        "}")
        self.nameLineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.nameLineEdit.setReadOnly(False)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.verticalLayout.addWidget(self.nameLineEdit)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.phoneLabel = QtWidgets.QLabel(profileDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phoneLabel.sizePolicy().hasHeightForWidth())
        self.phoneLabel.setSizePolicy(sizePolicy)
        self.phoneLabel.setStyleSheet("QLabel {\n"
                                      "    font: 87 8pt \"Arial Black\";\n"
                                      "    color: rgb(82, 30, 1);\n"
                                      "}")
        self.phoneLabel.setObjectName("phoneLabel")
        self.verticalLayout_5.addWidget(self.phoneLabel)
        self.phoneLineEdit = QtWidgets.QLineEdit(profileDialog)
        self.phoneLineEdit.setMinimumSize(QtCore.QSize(0, 31))
        self.phoneLineEdit.setMaximumSize(QtCore.QSize(16777215, 31))
        self.phoneLineEdit.setStyleSheet("QLineEdit {\n"
                                         "    \n"
                                         "    font: 8pt \"Arial\";\n"
                                         "    padding-left: 10px;\n"
                                         "    padding-right: 10px;\n"
                                         "    background-color: rgb(250, 235, 180);\n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QLineEdit:focus {\n"
                                         "  border: 2px solid rgb(250, 201, 131);\n"
                                         "}")
        self.phoneLineEdit.setReadOnly(False)
        self.phoneLineEdit.setObjectName("phoneLineEdit")
        self.verticalLayout_5.addWidget(self.phoneLineEdit)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.emailLabel = QtWidgets.QLabel(profileDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emailLabel.sizePolicy().hasHeightForWidth())
        self.emailLabel.setSizePolicy(sizePolicy)
        self.emailLabel.setStyleSheet("QLabel {\n"
                                      "    font: 87 8pt \"Arial Black\";\n"
                                      "    color: rgb(82, 30, 1);\n"
                                      "}")
        self.emailLabel.setObjectName("emailLabel")
        self.verticalLayout_2.addWidget(self.emailLabel)
        self.emailEdit = MuseLineEdit(profileDialog)
        self.emailEdit.setReadOnly(False)
        self.emailEdit.setObjectName("emailEdit")
        self.verticalLayout_2.addWidget(self.emailEdit)
        self.verticalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.passwordLabel = QtWidgets.QLabel(profileDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordLabel.sizePolicy().hasHeightForWidth())
        self.passwordLabel.setSizePolicy(sizePolicy)
        self.passwordLabel.setStyleSheet("QLabel {\n"
                                         "    font: 87 8pt \"Arial Black\";\n"
                                         "    color: rgb(82, 30, 1);\n"
                                         "}")
        self.passwordLabel.setObjectName("passwordLabel")
        self.verticalLayout_4.addWidget(self.passwordLabel)
        self.passwordLineEdit = QtWidgets.QLineEdit(profileDialog)
        self.passwordLineEdit.setMinimumSize(QtCore.QSize(0, 31))
        self.passwordLineEdit.setMaximumSize(QtCore.QSize(16777215, 31))
        self.passwordLineEdit.setStyleSheet("QLineEdit {\n"
                                            "    \n"
                                            "    font: 8pt \"Arial\";\n"
                                            "    padding-left: 10px;\n"
                                            "    padding-right: 10px;\n"
                                            "    background-color: rgb(250, 235, 180);\n"
                                            "    border-radius: 10px;\n"
                                            "}\n"
                                            "\n"
                                            "QLineEdit:focus {\n"
                                            "  border: 2px solid rgb(250, 201, 131);\n"
                                            "}")
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.verticalLayout_4.addWidget(self.passwordLineEdit)
        self.passwordVisibleCheckBox = QtWidgets.QCheckBox(profileDialog)
        self.passwordVisibleCheckBox.setStyleSheet("\n"
                                                   "\n"
                                                   "padding-left: 5px;\n"
                                                   "font: 8pt \"Arial Black\";")
        self.passwordVisibleCheckBox.setTristate(False)
        self.passwordVisibleCheckBox.setObjectName("passwordVisibleCheckBox")
        self.verticalLayout_4.addWidget(self.passwordVisibleCheckBox)
        self.confirmPasswordLabel = QtWidgets.QLabel(profileDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirmPasswordLabel.sizePolicy().hasHeightForWidth())
        self.confirmPasswordLabel.setSizePolicy(sizePolicy)
        self.confirmPasswordLabel.setStyleSheet("QLabel {\n"
                                                "    font: 87 8pt \"Arial Black\";\n"
                                                "    color: rgb(82, 30, 1);\n"
                                                "}")
        self.confirmPasswordLabel.setObjectName("confirmPasswordLabel")
        self.verticalLayout_4.addWidget(self.confirmPasswordLabel)
        self.confirmPasswordLineEdit = QtWidgets.QLineEdit(profileDialog)
        self.confirmPasswordLineEdit.setEnabled(False)
        self.confirmPasswordLineEdit.setMinimumSize(QtCore.QSize(0, 31))
        self.confirmPasswordLineEdit.setMaximumSize(QtCore.QSize(16777215, 31))
        self.confirmPasswordLineEdit.setStyleSheet("QLineEdit {\n"
                                                   "    \n"
                                                   "    font: 8pt \"Arial\";\n"
                                                   "    padding-left: 10px;\n"
                                                   "    padding-right: 10px;\n"
                                                   "    background-color: rgb(250, 235, 180);\n"
                                                   "    border-radius: 10px;\n"
                                                   "}\n"
                                                   "\n"
                                                   "QLineEdit:focus {\n"
                                                   "  border: 2px solid rgb(250, 201, 131);\n"
                                                   "}\n"
                                                   "\n"
                                                   "QLineEdit:!enabled {\n"
                                                   "    \n"
                                                   "    background: rgba(160, 160, 160, 100);\n"
                                                   "    font: 87 8pt \"Arial Black\";\n"
                                                   "    border: 1px solid rgb(150, 150, 150);\n"
                                                   "    border-radius: 10px;\n"
                                                   "    color: rgba(82, 30, 1, 100);\n"
                                                   "}")
        self.confirmPasswordLineEdit.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.confirmPasswordLineEdit.setObjectName("confirmPasswordLineEdit")
        self.verticalLayout_4.addWidget(self.confirmPasswordLineEdit)
        self.changeButton = QtWidgets.QPushButton(profileDialog)
        self.changeButton.setEnabled(False)
        self.changeButton.setMinimumSize(QtCore.QSize(100, 31))
        self.changeButton.setMaximumSize(QtCore.QSize(16777215, 31))
        self.changeButton.setStyleSheet("QWidget {\n"
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
                                                "  border: 2px solid rga(250, 201, 131);\n"
                                                "}\n"
                                                "\n"
                                                "\n"
                                                "\n"
                                                "QPushButton:!enabled {\n"
                                                "    \n"
                                                "    background: rgba(160, 160, 160, 100);\n"
                                                "    font: 87 8pt \"Arial Black\";\n"
                                                "    border: 1px solid rgb(150, 150, 150);\n"
                                                "    border-radius: 10px;\n"
                                                "    color: rgba(82, 30, 1, 100);\n"
                                                "}")
        self.changeButton.setObjectName("changePasswordButton")
        self.verticalLayout_4.addWidget(self.changeButton)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.closeProfileButton = QtWidgets.QPushButton(profileDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeProfileButton.sizePolicy().hasHeightForWidth())
        self.closeProfileButton.setSizePolicy(sizePolicy)
        self.closeProfileButton.setMinimumSize(QtCore.QSize(100, 31))
        self.closeProfileButton.setMaximumSize(QtCore.QSize(16777215, 31))
        self.closeProfileButton.setStyleSheet("QWidget {\n"
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
        self.closeProfileButton.setObjectName("closeProfileButton")
        self.confirmPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verticalLayout_6.addWidget(self.closeProfileButton)

        self.retranslateUi(profileDialog)
        QtCore.QMetaObject.connectSlotsByName(profileDialog)

    def retranslateUi(self, profileDialog):
        _translate = QtCore.QCoreApplication.translate
        profileDialog.setWindowTitle(_translate("profileDialog", "Просмотр профиля"))
        self.employeeLabel.setText(_translate("profileDialog", "Профиль"))
        self.fullnameLabel.setText(_translate("profileDialog", "Фио:"))
        self.emailLabel.setText(_translate("profileDialog", "Электронная почта:"))
        self.phoneLabel.setText(_translate("profileDialog", "Номер телефона:"))
        self.passwordLabel.setText(_translate("profileDialog", "Пароль:"))
        self.passwordVisibleCheckBox.setText(_translate("profileDialog", "Видимость пароля"))
        self.confirmPasswordLabel.setText(_translate("profileDialog", "Подтвердить пароль:"))
        self.changeButton.setText(_translate("profileDialog", "Изменить"))
        self.closeProfileButton.setText(_translate("profileDialog", "Закрыть"))
        self.closeProfileButton.setShortcut(_translate("profileDialog", "Ctrl+S"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    profileDialog = QtWidgets.QDialog()
    ui = ProfileWindowView()
    ui.setupUi(profileDialog)
    profileDialog.show()
    sys.exit(app.exec_())
