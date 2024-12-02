import sys

from PyQt5.QtWidgets import QApplication

from src.LoginScreen import LoginScreen


def window():
    app = QApplication(sys.argv)

    w = LoginScreen()
    w.show()
    status = app.exec_()
    sys.exit(status)


if __name__ == '__main__':

    window()