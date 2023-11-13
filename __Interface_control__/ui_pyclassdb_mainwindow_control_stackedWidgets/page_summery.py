from __Interface__.ui_pyclassdb_mainwindow import Ui_MainWindow

class page_summery:
    def __init__(self, mainUI:Ui_MainWindow) -> None:
        self.mainUI = mainUI

    def summeryBackBtn_clicked(self):
        self.mainUI.stackedWidget.setCurrentIndex(4)