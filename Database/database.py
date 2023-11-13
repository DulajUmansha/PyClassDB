from PySide6.QtSql import QSqlDatabase
from Database.host import Host
from Database.credential import Credential


class Database:
    def __init__(self) -> None:
        self.databaseName = None
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.host = Host()
        self.credential = Credential()

    def get_databaseName(self):
        return self.databaseName

    def set_databaseName(self, value):
        self.databaseName = value

    def connect(self):
        self.db.setHostName(self.host.get_hostName())
        self.db.setDatabaseName(self.databaseName)
        self.db.setUserName(self.credential.get_user_name())
        self.db.setPassword(self.credential.get_password())
        self.db.open()

    def close(self):
        self.db.close()
