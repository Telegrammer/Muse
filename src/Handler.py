from PyQt5.QtWidgets import QWidget

from .Emitters import VoidEmitter


class HideWidgetsHandler:

    def __init__(self, parent: QWidget):
        self.__parent: QWidget = parent
        self.__children: list[tuple[QWidget, VoidEmitter]] = []

    def add_widget(self, widget: QWidget, hide_emitter: VoidEmitter):
        hide_emitter.signal.connect(lambda: self.activation_change(widget))
        self.__children.append((widget, hide_emitter))

    def activation_change(self, sender: QWidget):

        sender.setHidden(True)
        if sender is self.__parent:
            for i in range(len(self.__children)):
                self.__children[i][0].setHidden(False)
        elif all([elem[0].isHidden() for elem in self.__children]):
            self.__parent.setHidden(False)
            self.__children = []
        print([elem[0].isHidden() for elem in self.__children],  all([elem[0].isHidden() for elem in self.__children]))
