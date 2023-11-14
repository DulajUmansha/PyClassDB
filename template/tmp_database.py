import os
from Database.credential import Credential
from Database.database import Database
from Database.host import Host

class Tmp_Database:
    def __init__(self) -> None:
        self.parent_code = None
    
    def load_the_code(self, host:Host, credential:Credential, database:Database):
        self.parent_code ="""
from PySide6.QtSql import QSqlDatabase

class Database:
    def __init__(self) -> None:
        self.db_host_name = """ "'{}'".format(host.get_hostName())+\
"""     
        self.db_name = """ "'{}'".format(database.get_databaseName())+\
"""     
        self.db_user_name = """ "'{}'".format(credential.get_user_name())+\
"""     
        self.db_password = """ "'{}'".format(credential.get_password())+\
"""     
        self.db = QSqlDatabase.addDatabase("QMYSQL")   

    def get_db_host_name(self) -> str:
        return self.db_host_name

    def set_db_host_name(self, value) -> None:
        self.db_host_name = value

    def get_db_name(self) -> str:
        return self.db_name

    def set_db_name(self, value) -> None:
        self.db_name = value

    def get_db_user_name(self) -> str:
        return self.db_user_name

    def set_db_user_name(self, value) -> None:
        self.db_user_name = value

    def get_db_password(self) -> str:
        return self.db_password

    def set_db_password(self, value) -> None:
        self.db_password = value

    def connect(self) -> None:
        self.db.setHostName(self.db_host_name)
        self.db.setDatabaseName(self.db_name)
        self.db.setUserName(self.db_user_name)
        self.db.setPassword(self.db_password)
        self.db.open()

    def close(self):
        self.db.close()
        """
    def generate(self, host:Host, credential:Credential, database:Database):
        self.load_the_code(host, credential, database)
        self.createFolder("output/database/")
        file = open('output//database//database.py','w')
        file.write(self.parent_code)
        file.close()
        
    def createFolder(self,path):
        if not os.path.exists(path):
            os.makedirs(path)
        return