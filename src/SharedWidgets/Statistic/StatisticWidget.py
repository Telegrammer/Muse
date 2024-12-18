import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QDialog

from src.SharedWidgets.Statistic.StatisticWidgetView import StatisticWidgetView


class StatisticWidget(QDialog, StatisticWidgetView):

    def get_cmap(self, n, name='hsv'):
        '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct
        RGB color; the keyword argument name must be a standard mpl colormap name.'''
        return plt.cm.get_cmap(name, n)

    def __init__(self, popular_exhibits: tuple[str, int], parent: QObject = None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.__names = [exhibit[0] for exhibit in popular_exhibits]
        self.__max_letters_count = 6

        self.__counts = np.array([exhibit[1] for exhibit in popular_exhibits])
        self.plot_on_canvas()

    def plot_on_canvas(self):
        self.figure.clear()
        plot_names = self.__names[:]
        for i in range(len(plot_names)):
            if len(plot_names[i]) < self.__max_letters_count:
                continue
            plot_names[i] = plot_names[i][:self.__max_letters_count] + "..."

        plt.bar(plot_names, self.__counts, color='brown', width=0.4)
        plt.xlabel("Экспонаты")
        plt.ylabel("Частота появления")
        self.canvas.draw()

    def resizeEvent(self, a0, QResizeEvent=None):
        self.__max_letters_count = 3 + ((self.width() - 600) // 100)
        if self.__max_letters_count > 35:
            self.__max_letters_count = 35
        self.plot_on_canvas()
