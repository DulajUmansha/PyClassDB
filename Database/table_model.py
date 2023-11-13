from PySide6.QtCore import Qt, QAbstractTableModel

class TableModel(QAbstractTableModel):
    def __init__(self, data:list, columnNames:list):
        super(TableModel, self).__init__()
        self._data = data
        self.numOfColumns = len(columnNames)
        self.horizontalHeaders = [''] * self.numOfColumns
        for columnNo, columnName in enumerate(columnNames):
            self.setHeaderData(columnNo, Qt.Horizontal, columnName)
    
    def setHeaderData(self, section, orientation, data, role=Qt.EditRole):
        if orientation == Qt.Horizontal and role in (Qt.DisplayRole, Qt.EditRole):
            try:
                self.horizontalHeaders[section] = data
                return True
            except:
                return False
        return super().setHeaderData(section, orientation, data, role)

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            try:
                return self.horizontalHeaders[section]
            except:
                pass
        return super().headerData(section, orientation, role)

    def data(self, index, role=0):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
            
    def rowCount(self, index=0):
        return len(self._data)

    def columnCount(self, index=0):
        return self.numOfColumns
        
  