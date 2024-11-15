from abc import abstractmethod

from PyQt5.QtCore import QObject
from PyQt5.QtCore import QObject

from src.Emitters import AbstractEmitter, TupleEmitter, StringEmitter, VoidEmitter

__all__ = ["QObject", "MuseDataSource", "AbstractEmitter", "TupleEmitter", "StringEmitter", "VoidEmitter"]


class MuseDataSource(QObject):

    def __init__(self):
        QObject.__init__(self, None)

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def return_data_before_destroy(self):
        pass
