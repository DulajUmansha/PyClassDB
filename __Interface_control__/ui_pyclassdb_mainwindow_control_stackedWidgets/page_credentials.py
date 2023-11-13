from __Interface__.ui_pyclassdb_mainwindow import Ui_MainWindow
from Database.credential import Credential

class page_credentials:
    def __init__(self, mainUI:Ui_MainWindow) -> None:
        self.mainUI = mainUI
        self.credential = Credential()

    def credentialNextBtn_clicked(self):
        self.mainUI.stackedWidget.setCurrentIndex(3)
        userName = self.mainUI.lineEdit_userName.text()
        password = self.mainUI.lineEdit_password.text()
        self.credential.set_user_name(userName)
        self.credential.set_password(password)

    def credentialBackBtn_clicked(self):
        self.mainUI.stackedWidget.setCurrentIndex(1)