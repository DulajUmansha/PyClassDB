from __Interface__.ui_pyclassdb_mainwindow import Ui_MainWindow
from Database.host import Host

class page_host:
    def __init__(self, mainUI:Ui_MainWindow,host:Host) -> None:
        self.mainUI = mainUI
        self.host = host

    def hostNextBtn_clicked(self):
        self.mainUI.stackedWidget.setCurrentIndex(2)
        hostName = self.mainUI.lineEdit_host.text()
        self.host.set_hostName(hostName)
    
    def hostBackBtn_clicked(self):
        self.mainUI.stackedWidget.setCurrentIndex(0)
