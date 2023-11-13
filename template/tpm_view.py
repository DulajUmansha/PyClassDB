class Tmp_View:
    def __init__(self) -> None:
        self.parent_code = None
        self.child_code = None

    def load_the_parentCode(self):
        self.parent_code = """ 
from PySide6.QtSql import  QSqlQueryModel

class View:
    def __init__(self):
        self.query = None

    def model(self):
        self.queryModel = QSqlQueryModel()
        self.queryModel.setQuery(self.query)
        return self.queryModel
    
    def get_query(self):
        return self.query

    def set_query(self, value):
        self.query = value
        """

    def load_the_childCode(self):
        self.child_code = """
        """

    def generate_parent(self):
        self.load_the_parentCode()
        file = open('view.py','w')
        file.write(self.parent_code)
        file.close()

    def generate_child(self):
        pass