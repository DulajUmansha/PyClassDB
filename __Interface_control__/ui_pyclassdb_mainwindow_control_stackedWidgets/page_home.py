from __Interface__.ui_pyclassdb_mainwindow import Ui_MainWindow

class page_home:
    def __init__(self, mainUI:Ui_MainWindow) -> None:
        self.mainUI = mainUI

    def getStartBtn_clicked(self):
        self.mainUI.stackedWidget.setCurrentIndex(1)

