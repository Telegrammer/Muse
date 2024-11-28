from PyQt5.QtCore import QSize, QRect
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QSpacerItem, QSizePolicy, QApplication, QVBoxLayout, QWidget, \
    QScrollArea

from src.Emitters import TupleEmitter
from src.SharedWidgets.MuseButton import MuseButton
from src.SharedWidgets.MuseComboBox import MuseComboBox
from src.SharedWidgets.MuseDialog.MuseDialogWidget import MuseDialog
from src.SharedWidgets.MuseLabel import MuseLabel
from src.SharedWidgets.MuseLineEdit import MuseLineEdit
from src.SharedWidgets.MusePeriodWidget import MusePeriodWidget
from src.SharedWidgets.MuseTableWidget import MuseTableWidget


class MuseFindDialogView(object):

    def setup_ui(self, dialog_window: QDialog, layout: QVBoxLayout):
        self.headerLayout = QHBoxLayout()
        self.headerLayout.setObjectName("headerLayout")
        self.headerLabel = MuseLabel("Поиск", dialog_window)

        self.headerLayout.addWidget(self.headerLabel)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.headerLayout.addItem(spacerItem)
        spacerItem1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)
        layout.addLayout(self.headerLayout)

        self.availableFiltersLayout = QHBoxLayout()
        self.filterLabel = MuseLabel("Доступные фильтры", dialog_window)
        self.availableFiltersLayout.addWidget(self.filterLabel)
        self.filterComboBox = MuseComboBox(rect=QRect(10, 10, 100, 250), parent=dialog_window)
        self.availableFiltersLayout.addWidget(self.filterComboBox)
        layout.addLayout(self.availableFiltersLayout)

        self.filterButtonsLayout = QHBoxLayout()
        self.addFilterButton = MuseButton("Добавить фильтр", dialog_window)
        self.filterButtonsLayout.addWidget(self.addFilterButton)
        self.filterButtonsLayout.setObjectName("filterButtonsLayout")
        self.removeFilterButton = MuseButton("Убрать фильтр", dialog_window)
        self.removeFilterButton.setEnabled(True)
        self.filterButtonsLayout.addWidget(self.removeFilterButton)
        layout.addLayout(self.filterButtonsLayout)
        spacerItem2 = QSpacerItem(20, 40, QSizePolicy.Minimum,
                                  QSizePolicy.MinimumExpanding)

        self.scrollArea = QScrollArea(dialog_window)
        self.scrollArea.setStyleSheet("border: 0px solid;\n"
                                      "QAbstractScrollArea {\n"
                                      "    \n"
                                      "    border-radius: 10px;\n"
                                      "}\n"
                                      "\n"
                                      " QScrollBar::handle:vertical {\n"
                                      "    background: #fac983\n"
                                      " }")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QWidget()
        self.data_sources_layout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 812, 729))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        layout.addWidget(self.scrollArea)


class MuseFindDialog(MuseDialog, MuseFindDialogView):

    def __init__(self, size: QSize, attributes: dict[str, MuseTableWidget.ItemType], parent_signal: TupleEmitter):
        super().__init__(size, parent_signal)
        self.set_layout(QVBoxLayout(self))
        MuseFindDialogView.setup_ui(self, self, self._layout)
        self._layout.addWidget(self._confirm_button)
        self._confirm_button.setText("Найти")

        self.__scroll_area_layouts = []
        self.__attribute_types: dict[str, MuseTableWidget.ItemType] = {}

        self.filterComboBox.addItems(list(attributes.keys()))
        self.__attribute_types = attributes

        self.__active_filters: list[str] = []

        self.addFilterButton.clicked.connect(self.add_filter)
        self.filterComboBox.activated.connect(self.add_filter)
        self.removeFilterButton.clicked.connect(self.remove_filter)
        self.removeFilterButton.setEnabled(False)

    def add_filter(self):
        self.__scroll_area_layouts.append([])

        header: str = self.filterComboBox.currentText()
        self.filterComboBox.removeItem(self.filterComboBox.currentIndex())
        self.__active_filters.append(header)

        data_source_layout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.__scroll_area_layouts[-1].append(data_source_layout)

        label = MuseLabel(header, self.scrollAreaWidgetContents)
        self.__scroll_area_layouts[-1].append(label)

        data_source_layout.addWidget(label)
        match self.__attribute_types[header]:
            case MuseTableWidget.ItemType.dateType:
                data_source = MusePeriodWidget(self.scrollAreaWidgetContents)
            case _:
                data_source = MuseLineEdit(self.scrollAreaWidgetContents)
        self.__scroll_area_layouts[-1].append(data_source)
        data_source_layout.addWidget(data_source)

        self.data_sources_layout.addLayout(data_source_layout)
        self.add_data_source(data_source)
        self.removeFilterButton.setEnabled(True)
        if self.filterComboBox.currentIndex() == -1:
            self.addFilterButton.setEnabled(False)

    def remove_filter(self):
        self.__scroll_area_layouts[-1][0].removeWidget(self.__scroll_area_layouts[-1][1])
        self.__scroll_area_layouts[-1][0].removeWidget(self.__scroll_area_layouts[-1][2])
        self.__scroll_area_layouts.pop(-1)

        self.filterComboBox.addItem(self.__active_filters.pop(-1))
        self._data_sources.pop(-1)

        if len(self._data_sources) == 0:
            self.removeFilterButton.setEnabled(False)
        self.addFilterButton.setEnabled(True)

    def _send_data(self):
        data_results = list(data_source.get_data() for data_source in self._data_sources)
        for i in range(len(data_results)):
            if self.__attribute_types[self.__active_filters[i]] != MuseTableWidget.ItemType.dateType:
                data_results[i] = f"like '%{data_results[i]}%'"

        data_results = [(self.__active_filters[i].replace(" ", ""), data_results[i]) for i in range(len(data_results))]

        self._data_transfer.signal.emit(tuple(data_results))
        self.close()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    formDialogWindow = MuseFindDialog(QSize(800, 600), {"Название": MuseTableWidget.ItemType.varchar},
                                      TupleEmitter(None))
    formDialogWindow.show()
    sys.exit(app.exec_())
