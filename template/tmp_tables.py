class Tmp_Tables:
    def __init__(self) -> None:
        self.parent_code = None
        self.child_code = None

    def load_the_parentCode(self):
        self.parent_code = """ 
from PySide6.QtSql import QSqlTableModel, QSqlQueryModel, QSqlQuery

class Table:
    def __init__(self) -> None:
        super(Table,self).__init__()
        self.tableName = None
        self.data = {}
        self.conditionColumnName = None
        self.conditionColumnData = None
        self.columnFilter = []

    def get_columnFilter(self) -> list:
        return self.columnFilter

    def set_columnFilter(self, value:list):#column Names 
        self.columnFilter = value

    def get_conditionData(self):
        return [self.conditionColumnName, self.conditionColumnData]

    def set_conditionData(self, columnName:str, columnData):
        self.conditionColumnName = columnName
        self.conditionColumnData = columnData

    def get_data(self) -> dict:
        return self.data

    def set_data(self, value:dict) -> None:
        self.data = value

    def get_tableName(self) -> str:
        return self.tableName

    def set_tableName(self, value) -> None:
        self.tableName = value

    def createTable(self) -> bool:
        pass

    def insertData(self, table=None, *args, **kwargs) -> bool:
        values = None
        if not table:
            table = self.tableName
        query = "INSERT INTO `%s` " % table
        if kwargs:
            keys = tuple(kwargs.keys())
            values = tuple(kwargs.values())
            query += "(" + ",".join(["%s"] * len(keys)) %  keys + ") VALUES (" + ",".join(["'%s'"]*len(values)) % values + ")"
        elif args:
            values = args
            query += " VALUES(" + ",".join(["%s"]*len(values)) + ")"
        print(query)
        Qquery = QSqlQuery()
        return(Qquery.exec(query))

    def retriveData(self, table=None , *args, **kwargs):
        filteredresult = {}
        query = 'SELECT '
        if args:
            keys = args
            values = tuple(kwargs.values())
            l = len(keys) - 1
            for i, key in enumerate(keys):
                query += "`"+key+"`"
                if i < l:
                    query += ","
        elif self.columnFilter:
            l = len(self.columnFilter) - 1
            for i, colunm in enumerate(self.columnFilter):
                query += "`"+colunm+"`"
                if i < l:
                    query += ","
        else:
           query += "* " 

        if table:
            query += ' FROM {}'.format(table)
        else:
           query += ' FROM {}'.format(self.tableName)

        if kwargs:
            self.conditionColumnName = tuple(kwargs.keys())[0]
            self.conditionColumnData =tuple(kwargs.values())[0]
            query += " WHERE `{}` = '{}'".format(self.conditionColumnName,
                                                 self.conditionColumnData)
            query += " AND `status` = 'active'"

        elif self.conditionColumnName and self.conditionColumnData:
            query += " WHERE `{}` = '{}'".format(self.conditionColumnName,
                                                 self.conditionColumnData)
            query += " AND `status` = 'active'"
            
        else:
            query += " WHERE `status` = 'active'"
    
        query = QSqlQuery(query)

        if len(self.columnFilter)<=0:
            tableColumnQuery = "SHOW columns FROM {}".format(self.tableName)
            tableColumnQuery = QSqlQuery(tableColumnQuery)
            while tableColumnQuery.next():
                fieldData = tableColumnQuery.record().indexOf('Field')
                self.columnFilter.append(tableColumnQuery.value(fieldData))

        result = []
        while query.next():
            for filteredColumn in self.columnFilter:
                fieldData = query.record().indexOf(filteredColumn)
                fieldResult = query.value(fieldData)
                filteredresult[filteredColumn] = fieldResult
            if self.conditionColumnData == None:
                result.append(filteredresult.copy())
        if self.conditionColumnData:
            return filteredresult
        else:
            return result

    def updateData(self, table, where=None, **kwargs) -> bool:
        if not table:
            table = self.tableName
        query  = "UPDATE %s SET " % table

        if kwargs:
            keys   = kwargs.keys()
            values = tuple(kwargs.values())
            l = len(keys) - 1
            for i, key in enumerate(keys):
                query += "`"+key+"` = '{}'".format(values[i])
                if i < l:
                    query += ","
            
        query += " WHERE `{}` = '{}'".format(self.conditionColumnName,
                                                 self.conditionColumnData)
        Qquery = QSqlQuery()
        return(Qquery.exec(query))

        """

    def load_the_childCode(self):
        self.child_code = """
        """

    def generate_parent(self):
        self.load_the_parentCode()
        file = open('table.py','w')
        file.write(self.parent_code)
        file.close()

    def generate_child(self):
        pass