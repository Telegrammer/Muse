from PyQt5.QtWidgets import QDialog, QWidget

from .RoleDecisionWidgetView import RoleDecisionWidgetView
from ..Emitters import StringEmitter


class RoleDecisionWidget(QDialog, RoleDecisionWidgetView):

    def __init__(self, parent: QWidget = None, parent_signal: StringEmitter = StringEmitter(None)):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setModal(True)
        self.setWindowTitle("Выбор роли")

        self.__parent_signal = parent_signal
        self.donatorRoleButton.clicked.connect(lambda: self.send_data("даритель"))
        self.employeeRoleButton.clicked.connect(lambda: self.send_data("сотрудник"))

    def send_data(self, data: str):
        self.__parent_signal.signal.emit(data)
        self.close()
