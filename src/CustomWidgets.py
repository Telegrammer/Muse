# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formDialogWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

__all__ = ["MuseButton", "MuseLabel", "MuseLineEdit", "MuseDialog"]

from PyQt5 import QtCore, QtWidgets


class MuseButton(QtWidgets.QPushButton):

    def __init__(self, text: str, object_name: str, parent: QtCore.QObject = None):
        QtWidgets.QPushButton.__init__(self, parent)

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(size_policy)
        self.setStyleSheet("QWidget {\n"
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

        self.setMinimumSize(QtCore.QSize(len(text) * 8, 31))
        self.setMaximumSize(QtCore.QSize(16777215, 31))
        self.setObjectName(object_name)
        self.setText(text)


class MuseLineEdit(QtWidgets.QLineEdit):

    def __init__(self, object_name: str, parent: QtCore.QObject = None):
        QtWidgets.QLineEdit.__init__(self, parent)
        self.setMinimumSize(QtCore.QSize(10, 31))
        self.setMaximumSize(QtCore.QSize(16777215, 31))
        self.setStyleSheet("QLineEdit {\n"
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
        self.setObjectName(object_name)


class MuseLabel(QtWidgets.QLabel):
    def __init__(self, label_text: str, object_name: str, parent: QtCore.QObject = None):
        QtWidgets.QLabel.__init__(self, parent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(8 * len(label_text), 40))
        self.setStyleSheet("QLabel {\n"
                           "    font: 87 8pt \"Arial Black\";\n"
                           "    color: rgb(82, 30, 1);\n"
                           "}")
        self.setObjectName(object_name)
        self.setText(label_text)


class MuseDialog(QtWidgets.QDialog):
    def __init__(self, size: QtCore.QSize, object_name: str, parent: QtCore.QObject = None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setObjectName(object_name)
        self.resize(size)
        self.setStyleSheet("QMenuBar {\n"
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


class Ui_formDialogWindow(object):
    def setupUi(self, formDialogWindow):
        self.verticalLayout = QtWidgets.QVBoxLayout(formDialogWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.templateLabel = MuseLabel("asdasdsad", "dsdasda", formDialogWindow)
        self.fffffffffffffffffffffff = QtWidgets.QLabel(formDialogWindow)
        self.verticalLayout.addWidget(self.templateLabel)
        self.templateLineEdit = MuseLineEdit("templateLineEdit")
        self.verticalLayout.addWidget(self.templateLineEdit)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem1)
        self.templateButton = MuseButton("Назначить экскурсоводом", "templateButton", formDialogWindow)
        self.verticalLayout.addWidget(self.templateButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.retranslateUi(formDialogWindow)
        QtCore.QMetaObject.connectSlotsByName(formDialogWindow)

    def retranslateUi(self, formDialogWindow):
        _translate = QtCore.QCoreApplication.translate
        formDialogWindow.setWindowTitle(_translate("formDialogWindow", "Form"))

        self.templateButton.setShortcut(_translate("formDialogWindow", "Ctrl+S"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    formDialogWindow = MuseWidget(QtCore.QSize(816, 300), "dsadasd")
    ui = Ui_formDialogWindow()
    ui.setupUi(formDialogWindow)
    formDialogWindow.show()
    sys.exit(app.exec_())