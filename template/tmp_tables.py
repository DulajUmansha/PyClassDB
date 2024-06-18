import os
from PySide6.QtSql import QSqlQuery


class Tmp_Tables:
    def __init__(self) -> None:
        self.parent_code = None
        self.child_code = None
        self._init_variables = []
        self.table_variable = []
        self.getter_setter = []
        self.retrive_variablesDict = []

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

        elif self.conditionColumnName and self.conditionColumnData:
            query += " WHERE `{}` = '{}'".format(self.conditionColumnName,
                                                 self.conditionColumnData)
            
        else:
            pass
    
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
                if values[i] == 'null':
                    query += "`"+key+"` = {}".format(values[i])
                else:
                    query += "`"+key+"` = '{}'".format(values[i])
                if i < l:
                    query += ","
            
        query += " WHERE `{}` = '{}'".format(self.conditionColumnName,
                                                 self.conditionColumnData)
        Qquery = QSqlQuery()
        return(Qquery.exec(query))

        """

    def load_the_childCode(self, tableName):
        self.child_code = (
            """from Database.table import Table

class """
            "{}".format(tableName)
            + """(Table):
\tdef __init__(self) -> None:
\t\tsuper("""
            "{}".format(tableName)
            + """,self).__init__()
\t\tself.tableName = """
            "'{}'".format(tableName)
            + """ #self.__class__.__name__
\t\t"""
        )
        for var in self._init_variables:
            self.child_code = self.child_code + var

        for func in self.getter_setter:
            self.child_code = self.child_code + func

        self.child_code = (
            self.child_code
            + """
\tdef retriveData(self):
\t\tself.set_tableName(self.tableName)
\t\tresult = super().retriveData()
\t\tif result == {}: return result
\t\tif type(result) == dict:"""
        )
        for retrive_varDict in self.retrive_variablesDict:
            self.child_code = self.child_code + retrive_varDict
        self.child_code = (
            self.child_code
            + """
\t\telif type(result) == list:"""
)
        for retrive_varList in self.retrive_variablesList:
            self.child_code = self.child_code + retrive_varList
        
        self.child_code = (
            self.child_code
            +"""
\t\treturn result

\tdef insertData(self, table=None, *args, **data) -> bool:
\t\tself.set_tableName(self.tableName)\n"""
            + "\t\tdata = {}".format(
                "{"
                + ",".join("'" + x + "'" + ":self." + x for x in self.table_variable)
                + "}|data"
            )
            + """
\t\tdata = {k: v for k, v in data.items() if v is not None}
\t\treturn super().insertData(table, *args, **data)

\tdef updateData(self, table=None, where=None, *args, **data) -> bool:
\t\tself.set_tableName(self.tableName)\n"""
            + "\t\tdata = {}".format(
                "{"
                + ",".join("'" + x + "'" + ":self." + x for x in self.table_variable)
                + "}|data"
            )
            + """
\t\tdata = {k: v for k, v in data.items() if v is not None}
\t\treturn super().updateData(table, where, *args, **data)
"""
        )

    def fetch_variables(self, tableName):
        self.table_variable = []
        tableColumnQuery = "SHOW columns FROM {}".format(tableName)
        tableColumnQuery = QSqlQuery(tableColumnQuery)
        while tableColumnQuery.next():
            fieldData = tableColumnQuery.record().indexOf("Field")
            self.table_variable.append(tableColumnQuery.value(fieldData))

    def load_the_childCode_variables(self):
        self._init_variables = []
        for var in self.table_variable:
            self._init_variables.append("self." + var + " = None\n\t\t")

    def load_getters_setters(self):
        self.getter_setter = []
        for var in self.table_variable:
            self.getter_setter.append(
                "\n\tdef get_{variable}(self):\n\t\treturn self.{variable}\n\n\tdef set_{variable}(self,value):\n\t\tself.{variable} = value\n".format(
                    variable=var
                )
            )

    def load_retrive_variablesforDict(self):
        self.retrive_variablesDict = []
        for var in self.table_variable:
            self.retrive_variablesDict.append(
                "\n\t\t\tif '{variable}' in result:\n\t\t\t\tself.{variable} = result['{variable}']".format(
                    variable=var
                )
            )

    def load_retrive_variablesforList(self):
        self.retrive_variablesList = []
        for var in self.table_variable:
            self.retrive_variablesList.append(
                "\n\t\t\t{variable}List = []".format(
                    variable=var
                )
            )
        self.retrive_variablesList.append("\n\t\t\tfor i in result:")
        for var in self.table_variable:
            self.retrive_variablesList.append(
                "\n\t\t\t\tif '{variable}' in i:\n\t\t\t\t\t{variable}List.append(i['{variable}'])".format(
                    variable=var
                )
            )
        for var in self.table_variable:
            self.retrive_variablesList.append(
                "\n\t\t\tself.{variable} = {variable}List".format(
                    variable=var
                )
            )

    def generate_parent(self):
        self.load_the_parentCode()
        self.createFolder("output/Database/")
        file = open("output//Database//table.py", "w")
        file.write(self.parent_code)
        file.close()

    def generate_child(self, tableNames):
        for tableName in tableNames:
            tableName = tableName[0]
            self.fetch_variables(tableName)
            self.load_the_childCode_variables()
            self.load_getters_setters()
            self.load_retrive_variablesforDict()
            self.load_retrive_variablesforList()
            self.load_the_childCode(tableName)
            self.createFolder("output/Database/")
            file = open("output//Database//{}.py".format(tableName), "w")
            file.write(self.child_code)
            file.close()

    def createFolder(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
        return
