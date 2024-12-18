from typing import Callable

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget, QAction, QShortcut

from src.Emitters import VoidEmitter, TupleEmitter
from src.SharedWidgets.MuseDialog.DialogFormFactory import DialogFormFactory
from src.SharedWidgets.MuseDialog.MuseFindDialogWidget import MuseFindDialog
from src.SharedWidgets.Profile.EmployeeProfile import EmployeeProfilePresenter
from src.SharedWidgets.Statistic.StatisticWidget import StatisticWidget
from .EditExcursionComposition import EditExcursionCompositionDialog
from .EditExhibitionComposition import EditExhibitionCompositionDialog
from .ManagerMainWindowView import ManagerMainWindowView
from .ManagerRepository import ManagerRepository
from ..SharedWidgets.MuseButton import MuseButton
from ..SharedWidgets.MuseDialog import MuseDialogWidget
from ..SharedWidgets.MuseTableWidget import MuseTableWidget

__all__ = ["ManagerMainWindow"]


class ManagerMainWindow(QMainWindow, ManagerMainWindowView):

    def __init__(self, parent_signal: VoidEmitter, user_data: tuple):
        QWidget.__init__(self, None)
        self.__user_data = user_data
        self.setupUi(self)
        self.update_tables()

        self.update_shortcut = QShortcut(QKeySequence("f5"), self)
        self.update_shortcut.activated.connect(self.update_tables)

        self.setVisibleExhibitionTableButton.clicked.connect(
            lambda: self.__set_visible_table(self.managerExhibitionTableWidget, self.selectExhibitionTableAction)
        )
        self.selectExhibitionTableAction.changed.connect(
            lambda: self.__set_visible_table(self.managerExhibitionTableWidget, self.selectExhibitionTableAction)
        )
        self.setVisibleExcursionTableButton.clicked.connect(
            lambda: self.__set_visible_table(self.managerExcursionTableWidget, self.selectExcursionTableAction)
        )
        self.selectExcursionTableAction.changed.connect(
            lambda: self.__set_visible_table(self.managerExcursionTableWidget, self.selectExcursionTableAction)
        )

        self.setVisibleAllExhibitionTableButton.clicked.connect(
            lambda: self.__set_visible_table(self.managerAllExhibitionTableWidget, QAction(None))
        )

        self.exhibitionTable.itemSelectionChanged.connect(
            lambda: self.__focus_change([self.editExhibitionButton,
                                         self.addExhibitionTableAction,
                                         self.deleteExhibitionTableAction],

                                        [self.editExcursionButton,
                                         self.addExcursionAction,
                                         self.removeExcursionAction])
        )
        self.exhibitionTable.itemSelectionChanged.connect(
            self.exhibitionTable.clearSelection
        )

        self.excursionTable.itemSelectionChanged.connect(
            lambda: self.__focus_change([self.editExcursionButton,
                                         self.addExcursionAction,
                                         self.removeExcursionAction],

                                        [self.editExhibitionButton,
                                         self.addExhibitionTableAction,
                                         self.deleteExhibitionTableAction]
                                        )
        )
        self.excursionTable.itemSelectionChanged.connect(
            lambda: self.excursionTable.clearSelection()
        )

        self.addExhibitionButton.clicked.connect(
            lambda: self.form_dialog("Добавить выставку", "Добавить", "Выставка",
                                     operation=self.add_exhibition, table=self.exhibitionTable, is_new_row=True)
        )
        self.addExhibitionTableAction.triggered.connect(
            lambda: self.form_dialog("Добавить выставку", "Добавить", "Выставка",
                                     operation=self.add_exhibition, table=self.exhibitionTable, is_new_row=True)
        )

        self.editExhibitionButton.clicked.connect(
            lambda: self.form_edit_exhibition_dialog("Изменить информацию о выставке", "Изменить", "Выставка",
                                                     operation=self.edit_exhibition, table=self.exhibitionTable,
                                                     is_new_row=False)
        )

        self.deleteExhibitionTableAction.triggered.connect(self.remove_exhibition)
        self.deleteExhibitionButton.clicked.connect(self.remove_exhibition)

        self.findExhibitionButton.clicked.connect(
            lambda: self.form_find_dialog("Найти выставку", operation=self.find_exhibitions, table=self.exhibitionTable)
        )
        self.findExhibitionTableAction.triggered.connect(
            lambda: self.form_find_dialog("Найти выставку", operation=self.find_exhibitions, table=self.exhibitionTable)
        )

        self.addExcursionButton.clicked.connect(
            lambda: self.form_dialog("Добавить экскурсию", "Добавить", "Экскурсия",
                                     operation=self.add_excursion, table=self.excursionTable, is_new_row=True)
        )
        self.addExcursionAction.triggered.connect(
            lambda: self.form_dialog("Добавить экскурсию", "Добавить", "Экскурсия",
                                     operation=self.add_excursion, table=self.excursionTable, is_new_row=True)
        )

        self.editExcursionButton.clicked.connect(
            lambda: self.form_edit_excursion_dialog("Изменить информацию об экскурсии", "Изменить", "Экскурсия",
                                                    operation=self.edit_excursion, table=self.excursionTable,
                                                    is_new_row=False)
        )

        self.removeExcursionAction.triggered.connect(self.remove_excursion)
        self.deleteExcursionButton.clicked.connect(self.remove_excursion)

        self.findExcursionButton.clicked.connect(
            lambda: self.form_find_dialog("Найти экскурсию", operation=self.find_excursions, table=self.excursionTable)
        )
        self.findExcursionAction.triggered.connect(
            lambda: self.form_find_dialog("Найти экскурсию", operation=self.find_excursions, table=self.excursionTable)
        )

        self.findAllExhibitionButton.clicked.connect(
            lambda: self.form_find_dialog("Найти выставку", operation=self.find_other_exhibitions,
                                          table=self.allExhibitionTable)
        )

        self.__quit_session_signal = parent_signal
        self.quitSessionAction.triggered.connect(
            lambda: self.__quit_session_signal.signal.emit()
        )

        self.viewProfileInfoAction.triggered.connect(self.open_profile)
        self.openStatisticButton.clicked.connect(self.open_statistics)

    def open_statistics(self):
        exhibits = ManagerRepository().identify_popular_exhibits()
        exhibits = [(exhibit[-2], exhibit[-1]) for exhibit in exhibits]
        statistics_window = StatisticWidget(exhibits)
        statistics_window.show()
        statistics_window.exec_()

    def open_profile(self):

        profile_window = EmployeeProfilePresenter(self.__user_data, self)
        profile_window.setModal(True)
        profile_window.show()
        profile_window.exec_()

    @staticmethod
    def __set_visible_table(table: QWidget, action: QAction):
        table_visible: bool = table.isVisible()
        action_status: bool = action.isChecked()
        if table_visible == action_status:
            action.setChecked(not action_status)
        table.setHidden(table_visible)

    @staticmethod
    def __focus_change(focused_widgets: list[QWidget], unfocused_widgets: list[QWidget]):
        for widget in focused_widgets:
            widget.setEnabled(True)
        for widget in unfocused_widgets:
            widget.setEnabled(False)

    def form_dialog(self,
                    window_title: str,
                    button_label: str,
                    table_name: str,
                    operation: Callable,
                    table: MuseTableWidget,
                    is_new_row: bool
                    ):
        dialog_factory: DialogFormFactory = DialogFormFactory(window_title, button_label, table_name,
                                                              table.get_row_data(is_new_row))
        send_data_signal = TupleEmitter(self)
        send_data_signal.signal.connect(operation)
        dialog_form = dialog_factory(send_data_signal)
        dialog_form.show()
        dialog_form.exec_()

    def form_edit_excursion_dialog(self,
                                   window_title: str,
                                   button_label: str,
                                   table_name: str,
                                   operation: Callable,
                                   table: MuseTableWidget,
                                   is_new_row: bool):
        dialog_factory: DialogFormFactory = DialogFormFactory(window_title, button_label, table_name,
                                                              table.get_row_data(is_new_row))
        send_data_signal = TupleEmitter(self)
        send_data_signal.signal.connect(operation)
        dialog_form: MuseDialogWidget = dialog_factory(send_data_signal)
        dialog_form.get_layout().removeWidget(dialog_form.get_confirm_button())

        change_excursion_items_button = MuseButton("Изменить состав экскурсии", dialog_form)
        change_excursion_items_button.clicked.connect(
            lambda: self.form_edit_excursion_composition_dialog("Изменить состав экскурсии", self.edit_excursion))
        dialog_form.get_layout().addWidget(change_excursion_items_button)
        dialog_form.get_layout().addWidget(dialog_form.get_confirm_button())
        dialog_form.show()
        dialog_form.exec_()

    def form_edit_excursion_composition_dialog(self, window_title: str, operation: Callable):
        send_data_signal = TupleEmitter(self)
        find_dialog_form = EditExcursionCompositionDialog(QSize(800, 800),
                                                          self.excursionTable.get_id(self.excursionTable.currentRow()),
                                                          {"Номер зала": MuseTableWidget.ItemType.varchar,
                                                           "Площадь": MuseTableWidget.ItemType.varchar,
                                                           "Высота": MuseTableWidget.ItemType.varchar,
                                                           "Местоположение": MuseTableWidget.ItemType.varchar}
                                                          , send_data_signal)
        find_dialog_form.setWindowTitle(window_title)
        find_dialog_form.setModal(True)
        find_dialog_form.exec_()

    def form_edit_exhibition_dialog(self,
                                    window_title: str,
                                    button_label: str,
                                    table_name: str,
                                    operation: Callable,
                                    table: MuseTableWidget,
                                    is_new_row: bool):
        dialog_factory: DialogFormFactory = DialogFormFactory(window_title, button_label, table_name,
                                                              table.get_row_data(is_new_row))
        send_data_signal = TupleEmitter(self)
        send_data_signal.signal.connect(operation)
        dialog_form: MuseDialogWidget = dialog_factory(send_data_signal)
        dialog_form.get_layout().removeWidget(dialog_form.get_confirm_button())

        change_exhibition_items_button = MuseButton("Изменить состав выставки", dialog_form)
        change_exhibition_items_button.clicked.connect(
            lambda: self.form_edit_exhibition_composition_dialog("Изменить состав выставки", self.edit_exhibition))
        dialog_form.get_layout().addWidget(change_exhibition_items_button)
        dialog_form.get_layout().addWidget(dialog_form.get_confirm_button())
        dialog_form.show()
        dialog_form.exec_()

    def form_edit_exhibition_composition_dialog(self, window_title: str, operation: Callable):
        send_data_signal = TupleEmitter(self)
        find_dialog_form = EditExhibitionCompositionDialog(QSize(1000, 800),
                                                           self.exhibitionTable.get_id(
                                                               self.exhibitionTable.currentRow()),
                                                           {"Наименование": MuseTableWidget.ItemType.varchar,
                                                            "Вид": MuseTableWidget.ItemType.enumType,
                                                            "Номер зала": MuseTableWidget.ItemType.enumType,
                                                            "Описание": MuseTableWidget.ItemType.varchar,
                                                            "Размер": MuseTableWidget.ItemType.varchar,
                                                            "Год создания": MuseTableWidget.ItemType.varchar,
                                                            "Происхождение": MuseTableWidget.ItemType.varchar}
                                                           , send_data_signal)
        find_dialog_form.setWindowTitle(window_title)
        find_dialog_form.setModal(True)
        find_dialog_form.exec_()

    def add_exhibition(self, dialog_output: tuple[str]):
        ManagerRepository().add_exhibition(self.__user_data[0],
                                           dialog_output[0],
                                           dialog_output[1],
                                           dialog_output[2],
                                           dialog_output[3],
                                           dialog_output[4])
        self.update_exhibition_table()

    def edit_exhibition(self, dialog_output: tuple[str]):
        ManagerRepository().edit_exhibition(self.exhibitionTable.get_id(self.exhibitionTable.currentRow()),
                                            dialog_output[0],
                                            dialog_output[1],
                                            dialog_output[2],
                                            dialog_output[3],
                                            dialog_output[4])
        self.update_exhibition_table()

    def remove_exhibition(self):
        ManagerRepository().remove_exhibition(self.exhibitionTable.get_id(self.exhibitionTable.currentRow()))
        self.update_exhibition_table()

    def find_exhibitions(self, dialog_output: tuple[str]):
        self.exhibitionTable.set_filters(dialog_output)
        self.update_exhibition_table(dialog_output)

    def find_other_exhibitions(self, dialog_output: tuple[str]):
        self.allExhibitionTable.set_filters(dialog_output)
        self.update_all_exhibitions_table(dialog_output)

    def add_excursion(self, dialog_output: tuple[str]):
        ManagerRepository().add_excursion(dialog_output[0], dialog_output[1], dialog_output[2], dialog_output[3])
        self.update_excursion_table()

    def edit_excursion(self, dialog_output: tuple[str]):
        row_data = self.excursionTable.get_row_data()

        attributes = [(dialog_output[i], row_data[i][1]) for i in range(len(row_data))]
        ManagerRepository().edit_excursion(attributes,
                                           excursion_id=self.excursionTable.get_id(self.excursionTable.currentRow()))
        self.update_excursion_table()

    def remove_excursion(self):
        ManagerRepository().remove_excursion(self.excursionTable.get_id(self.excursionTable.currentRow()))
        self.update_excursion_table()

    def find_excursions(self, dialog_output: tuple[str]):
        self.excursionTable.set_filters(dialog_output)
        self.update_excursion_table(dialog_output)

    def update_tables(self):
        self.update_exhibition_table()
        self.update_excursion_table()
        self.update_all_exhibitions_table()

    def update_all_exhibitions_table(self, filters=None, orders=None):
        self.allExhibitionTable.blockSignals(False)
        self.allExhibitionTable.setRowCount(0)
        self.allExhibitionTable.clear_ids()

        exhibitions = ManagerRepository().find_all_exhibitions(self.__user_data[0], filters=filters)
        for exhibition in exhibitions:
            self.allExhibitionTable.insertRow(self.allExhibitionTable.rowCount())
            self.allExhibitionTable.add_id(exhibition[0])
            self.allExhibitionTable.set_row(exhibition[1:])

        self.allExhibitionTable.blockSignals(False)

    def update_exhibition_table(self, filters=None, orders=None):
        self.exhibitionTable.blockSignals(True)
        self.exhibitionTable.setRowCount(0)
        self.exhibitionTable.clear_ids()

        exhibitions = ManagerRepository().find_exhibitions(self.__user_data[0], filters=filters)
        for exhibition in exhibitions:
            self.exhibitionTable.insertRow(self.exhibitionTable.rowCount())
            self.exhibitionTable.add_id(exhibition[0])
            self.exhibitionTable.set_row(exhibition[1:])

        self.exhibitionTable.blockSignals(False)
        self.__focus_change([],
                            [self.editExhibitionButton, self.addExhibitionTableAction,
                             self.deleteExhibitionTableAction])

    def update_excursion_table(self, filters=None, orders=None):
        self.excursionTable.blockSignals(True)
        self.excursionTable.setRowCount(0)
        self.excursionTable.clear_ids()
        excursions = ManagerRepository().find_excursions(filters=filters)
        for excursion in excursions:
            self.excursionTable.insertRow(self.excursionTable.rowCount())
            self.excursionTable.add_id(excursion[0])
            self.excursionTable.set_row(excursion[1:])
        self.excursionTable.set_attribute_values("Назначенный экскурсовод", ManagerRepository().get_guides())
        self.excursionTable.blockSignals(False)
        self.__focus_change([], [self.editExcursionButton, self.findExcursionAction, self.addExcursionAction,
                                 self.removeExcursionAction])

    def form_find_dialog(self, window_title: str, operation: Callable, table: MuseTableWidget):
        send_data_signal = TupleEmitter(self)
        send_data_signal.signal.connect(operation)
        find_dialog_form = MuseFindDialog(QSize(800, 600), table.get_attributes(), send_data_signal)
        find_dialog_form.setWindowTitle(window_title)
        find_dialog_form.setModal(True)
        find_dialog_form.exec_()
