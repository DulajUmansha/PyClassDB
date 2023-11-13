import sys
from PySide6.QtWidgets import QMainWindow
from Database.credential import Credential
from Database.database import Database
from Database.host import Host
from __Interface__.rc_resource import *
from __Interface__.ui_pyclassdb_mainwindow import Ui_MainWindow
from __Interface_control__.ui_pyclassdb_mainwindow_control_stackedWidgets.page_home import page_home
from __Interface_control__.ui_pyclassdb_mainwindow_control_stackedWidgets.page_host import page_host
from __Interface_control__.ui_pyclassdb_mainwindow_control_stackedWidgets.page_credentials import page_credentials
from __Interface_control__.ui_pyclassdb_mainwindow_control_stackedWidgets.page_database import page_database
from __Interface_control__.ui_pyclassdb_mainwindow_control_stackedWidgets.page_table import page_table
from __Interface_control__.ui_pyclassdb_mainwindow_control_stackedWidgets.page_summery import page_summery
from template.tmp_database import Tmp_Database
from template.tmp_tables import Tmp_Tables


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.mainUI = Ui_MainWindow()
        self.mainUI.setupUi(self)
        self.host = Host()
        self.credential = Credential()
        self.database = Database(self.host,self.credential)

        self.pageHome = page_home(self.mainUI)
        self.pageHost = page_host(self.mainUI,self.host)
        self.pageCredentials = page_credentials(self.mainUI,self.credential)
        self.pageDatabase = page_database(self.mainUI,self.database)
        self.pageTable = page_table(self.mainUI)
        self.pageSummery = page_summery(self.mainUI)
        self.buttonClicked_connect()

    def buttonClicked_connect(self):
        self.mainUI.getStartBtn.clicked.connect(self.pageHome.getStartBtn_clicked)
        self.mainUI.hostNextBtn.clicked.connect(self.pageHost.hostNextBtn_clicked)
        self.mainUI.hostBackBtn.clicked.connect(self.pageHost.hostBackBtn_clicked)
        self.mainUI.credentialNextBtn.clicked.connect(self.pageCredentials.credentialNextBtn_clicked)
        self.mainUI.credentialBackBtn.clicked.connect(self.pageCredentials.credentialBackBtn_clicked)
        self.mainUI.databaseNextBtn.clicked.connect(self.pageDatabase.databaseNextBtn_clicked)
        self.mainUI.databaseNextBtn.clicked.connect(self.pageTable.showTables)
        self.mainUI.databaseBackBtn.clicked.connect(self.pageDatabase.databaseBackBtn_clicked)
        self.mainUI.tableNextBtn.clicked.connect(self.tableNextBtn_clicked)
        self.mainUI.tableBackBtn.clicked.connect(self.pageTable.tableBackBtn_clicked)
        self.mainUI.summeryBackBtn.clicked.connect(self.pageSummery.summeryBackBtn_clicked)

    def tableNextBtn_clicked(self):
        tmpDatabase = Tmp_Database()
        tmpDatabase.generate(self.host, self.credential, self.database)

        tmpTable = Tmp_Tables()
        tmpTable.generate_parent()
        tmpTable.generate_child()#TODO
       


