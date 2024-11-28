# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formDialogWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

__all__ = ["MuseTableWidget"]

import sys
from enum import IntEnum

from PyQt5 import QtCore, QtWidgets


class MuseTableWidgetView(object):
    def setup_ui(self, table_widget: QtWidgets.QTableWidget, column_count, header_names: list[str]):
        table_widget.setStyleSheet("\n"
                                   "QTableWidgetItem {\n"
                                   "    font: 8pt \"Arial\";\n"
                                   "}\n"
                                   "\n"
                                   "QWidget {background-color: rgb(255, 245, 183);}\n"
                                   "\n"
                                   "QAbstractItemView {\n"
                                   "\n"
                                   "    font: 8pt \"Arial Black\";\n"
                                   "}\n"
                                   "\n"
                                   "QAbstractScrollArea {\n"
                                   "    \n"
                                   "    border-radius: 10px;\n"
                                   "}\n"
                                   "\n"
                                   " QScrollBar::handle:vertical {\n"
                                   "    background: #fac983\n"
                                   " }\n"
                                   "\n"
                                   "QScrollBar::handle:horizontal {\n"
                                   "    background: #fac983;\n"
                                   " }\n"
                                   "")
        table_widget.setColumnCount(column_count)
        for i in range(column_count):
            item: QtWidgets.QTableWidgetItem = QtWidgets.QTableWidgetItem()
            item.setText(header_names[i])
            table_widget.setHorizontalHeaderItem(i, item)


class MuseTableWidget(QtWidgets.QTableWidget, MuseTableWidgetView):
    class ItemType(IntEnum):
        varchar = 0
        integer = 1
        enumType = 2
        dateType = 3

    def __init__(self, attributes: dict[str, ItemType], parent=QtCore.QObject):
        QtWidgets.QTableWidget.__init__(self, parent)
        self.__attributes_count = len(attributes.keys())
        self.setup_ui(self, self.__attributes_count, [name for name in attributes.keys()])
        self.__attributes_enums: dict[str, list[str]] = {}
        self.__attributes: dict[str, MuseTableWidget.ItemType] = attributes

        self.__last_row = None
        self.__last_column = None
        self.__ids = []
        self.__filters = []

    def insertRow(self, row: int):
        QtWidgets.QTableWidget.insertRow(self, row)
        for i in range(self.__attributes_count):
            item: QtWidgets.QTableWidgetItem = QtWidgets.QTableWidgetItem()
            self.setItem(self.rowCount() - 1, i, item)

    def get_attributes(self):
        return self.__attributes

    def get_ids(self):
        return self.__ids

    def get_id(self, index: int):
        return self.__ids[index]

    def add_id(self, row_id: int):
        self.__ids.append(row_id)

    def remove_id(self, index: int):
        self.__ids.pop(index)

    def clear_ids(self):
        self.__ids = []

    def setItem(self, row: int, column: int, item: QtWidgets.QTableWidgetItem):
        attribute_type: MuseTableWidget.ItemType = self.__attributes[list(self.__attributes.keys())[column]]
        item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)
        QtWidgets.QTableWidget.setItem(self, row, column, item)

    def set_row(self, row_data: tuple):
        for i in range(self.columnCount()):
            self.setItem(self.rowCount() - 1, i, QtWidgets.QTableWidgetItem(row_data[i]))

    def insert_attribute(self, attribute_name: str, attribute_type: ItemType, column: int = None):

        if column is None:
            column = self.__attributes_count
        QtWidgets.QTableWidget.insertColumn(self, column)
        item: QtWidgets.QTableWidgetItem = QtWidgets.QTableWidgetItem()
        item.setText(attribute_name)
        self.__attributes[attribute_name] = attribute_type
        self.setHorizontalHeaderItem(column, item)
        for i in range(self.rowCount()):
            item: QtWidgets.QTableWidgetItem = QtWidgets.QTableWidgetItem()
            if column != self.__attributes_count:
                column += 1
            self.setItem(i, column, item)
        self.__attributes_count += 1

    def set_attribute_values(self, name: str, values: list[str]):
        self.__attributes_enums[name] = values

    def get_attribute_type(self, key: str):
        return self.__attributes[key]

    def get_attribute_enums(self, key: str) -> list[str]:
        try:
            return self.__attributes_enums[key]
        except KeyError:
            return []

    def get_row_data(self, is_new_row: bool = True) -> list[tuple[str]]:
        result: list[tuple[str, MuseTableWidget.ItemType, str, list[str]]] = []
        column_count: int = self.columnCount()
        if is_new_row:
            for i in range(column_count):
                header: str = self.horizontalHeaderItem(i).text()
                result.append((header,
                               self.get_attribute_type(header),
                               "",
                               self.get_attribute_enums(header)
                               ))
            return result

        selected_row: int = self.currentRow()

        for i in range(column_count):
            header: str = self.horizontalHeaderItem(i).text()
            try:
                result.append((header,
                               self.get_attribute_type(header),
                               self.item(selected_row, i).text(),
                               self.get_attribute_enums(header)
                               ))
            except AttributeError:
                result.append((header,
                               self.get_attribute_type(header),
                               "",
                               self.get_attribute_enums(header)
                               ))
        return result

    def get_row_range(self):
        return [model_index.row() for model_index in self.selectionModel().selectedRows()]

    def set_filters(self, filters: tuple[tuple[str, str]]):
        self.__filters = filters

    def get_filters(self):
        return self.__filters


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    w = MuseTableWidget({}, parent=None)

    w.insert_attribute("Фио", MuseTableWidget.ItemType.varchar)
    w.insert_attribute("Должность", MuseTableWidget.ItemType.enumType)
    w.insert_attribute("Дата рождения", MuseTableWidget.ItemType.dateType)
    w.insert_attribute("Номер телефона", MuseTableWidget.ItemType.varchar)
    w.set_attribute_values("Должность", ["Администратор", "Куратор", "Менеджер", "Экскурсовод"])
    w.set_attribute_values("Дата рождения", ["Администратор", "Куратор", "Менеджер", "Экскурсовод"])
    w.insertRow(w.rowCount())
    w.insertRow(w.rowCount())

    w.show()
    status = app.exec_()
    sys.exit(status)
