from __Interface__.ui_pyclassdb_mainwindow import Ui_MainWindow
from Database.database import Database

class page_database:
    def __init__(self, mainUI:Ui_MainWindow, database:Database) -> None:
        self.mainUI = mainUI
        self.database = database

    def databaseNextBtn_clicked(self):
        self.mainUI.stackedWidget.setCurrentIndex(4)
        databaseName = self.mainUI.lineEdit_database.text()
        self.database.set_databaseName(databaseName)
        self.database.connect()

    def databaseBackBtn_clicked(self):
        self.mainUI.stackedWidget.setCurrentIndex(2)