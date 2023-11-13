from Database.table_model import TableModel
from __Interface__.ui_pyclassdb_mainwindow import Ui_MainWindow
from PySide6.QtWidgets import QHeaderView
from PySide6.QtSql import QSqlQuery

class page_table:
    def __init__(self, mainUI:Ui_MainWindow) -> None:
        self.mainUI = mainUI
        self.tableNames = []

    def tableBackBtn_clicked(self):
        self.mainUI.stackedWidget.setCurrentIndex(3)

    def fetchTables(self):
        query = "SHOW tables"
        query = QSqlQuery(query)
        while query.next():
            self.tableNames.append([query.value(0)])

    def showTables(self):
        self.fetchTables()
        columns = ['Tables']
        table_model = TableModel(self.tableNames,columns)
        self.mainUI.tableView.setModel(table_model)
        self.mainUI.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.mainUI.tableView.show()