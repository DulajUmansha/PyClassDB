import sys
from PySide6.QtWidgets import QMainWindow
from __Interface__.rc_resource import *
from __Interface__.ui_pyclassdb_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.mainUI = Ui_MainWindow()
        self.mainUI.setupUi(self)


