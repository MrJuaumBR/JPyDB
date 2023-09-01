import pickle
import base64
import os

GSTRFTIME = "%d/%m/%Y %H:%I"
from datetime import datetime

from ._Exceptions import (TableNotFound, ColumnNotFound, ValueTypeIncorrect, IncorrectSizeColumnsAndValues)

class Columns_():
    def __init__(self,name:str, type:type, not_null:bool) -> None:
        self.column_name = name
        self.type = type
        self.not_null = not_null

        self.values = {}

    def add_value(self,id:any, value:any):
        if not str(id) in self.values.keys():
            if type(value) == self.type:
                self.values[str(id)] = value
            else:
                raise(ValueTypeIncorrect(str(id)))
        else:
            print(f'Value: {id}, Already in Column')

    def update_value(self, id:any, value:any):
        if str(id) in self.values.keys():
            if type(value) == self.type:
                self.values[str(id)] = value
            else:
                raise(ValueTypeIncorrect(str(id)))
        else:
            print(f'Value: {id}, Not Found in Column')

    def get_value(self, id:any) -> any:
        if str(id) in self.values.keys():
            return self.values[str(id)]
        else:
            print(f'Value: {id}, Not Found in Column')
            return None
     
class Tables_():
    def __init__(self,table_name:str) -> None:
        self.table_name = table_name

        self.columns = {}

    def ids_count(self) -> int:
        x = len(self.columns[next(iter(self.columns))].values)
        return x

    def add_column(self, column_name:str, type:type, null:bool):
        if not column_name in self.columns.keys():
            col = Columns_(column_name, type, null)
            self.columns[column_name] = col
        else:
            print(f'Column: {column_name}, Already in Table')

    def delete_column(self, column_name:str):
        if column_name in self.columns.keys():
            self.columns.pop(column_name)
        else:
            raise(ColumnNotFound(column_name))

    def add_value(self, column_name:str, id:int, value:any):
        if column_name in self.columns.keys():
            col:Columns_ = self.columns[column_name]
            col.add_value(id, value)
        else:
            raise(ColumnNotFound(column_name))

    def update_value(self, column_name:str, id:int, value:any):
        if column_name in self.columns.keys():
            col:Columns_ = self.columns[column_name]
            col.update_value(id, value)
        else:
            raise(ColumnNotFound(column_name))

    def get_value(self, column_name:str, id) -> any:
        if column_name in self.columns.keys():
            return self.columns[column_name].get_value(id)
        else:
            raise(ColumnNotFound(column_name))

    def get(self, id) -> any:
        g = {}
        for col in self.columns.keys():
            c:Columns_ = self.columns[col]
            if str(id) in c.values.keys():
                g[col] = c.get_value(id)
        return g

class Database_():
    """Database Cursor and controller"""
    def __init__(self,filename:str) -> None:
        self.CommonLoad = False
        if not filename in ['',' ', None]:
            self.CommonLoad = True
            self.filename=  "./"+str(filename)+".pydb"
        self.tables = {}

        self.created_at = datetime.now().strftime(GSTRFTIME)
        self.updated_at = ""

        if self.CommonLoad:
            self.startup()

    def ids_count(self, table_name:str) -> int:
        """Get lenght of values stored in a table"""
        if table_name in self.tables:
            return self.tables[table_name].ids_count()
        else:
            raise(TableNotFound(table_name))

    def add_column(self, table_name:str,name:str, type:type, null:bool):
        """Add a Column for a table"""
        if table_name in self.tables.keys():
            self.tables[table_name].add_column(name, type, null)
        else:
            raise(TableNotFound(table_name))

    def delete_column(self, table_name:str, column_name:str):
        """Delete a column from a table"""
        if table_name in self.tables.keys():
            self.tables[table_name].delete_column(column_name)
        else:
            raise(TableNotFound(table_name))

    def get(self, table_name, id) -> any:
        """Get all values by id"""
        if table_name in self.tables.keys():
            x:Columns_ = self.tables[table_name]
            return x.get(id)
        else:
            raise(TableNotFound(table_name))

    def get_value(self, table_name:str,column_name:str, id) -> any:
        """Get a value in a Table & Column"""
        if table_name in self.tables.keys():
            return self.tables[table_name].get_value(column_name, id)
        else:
            raise(TableNotFound(table_name))

    def add_value(self, table_name:str,column_name:str, id:int, value:any):
        """Add a value in a Table & Column"""
        if table_name in self.tables.keys():
            self.tables[table_name].add_value(column_name, id, value)
        else:
            raise(TableNotFound(table_name))
    
    def add_values(self, table_name:str,columns:list or tuple,values:list or tuple,id:int):
        """Add values for a id"""
        if table_name in self.tables.keys():
            if len(columns) == len(values):
                for x,item in enumerate(columns):
                    self.add_value(table_name,item,id,values[x])
            else:
                raise(IncorrectSizeColumnsAndValues(columns,values))
        else:
            raise(TableNotFound(table_name))
        
    def update_value(self, table_name:str,column_name:str, id:int, value:any):
        """Update a value in a table & Column"""
        if table_name in self.tables.keys():
            self.tables[table_name].update_value(column_name, id, value)
        else:
            raise(TableNotFound(table_name))

    def delete_table(self, table_name:str):
        """Delete a table"""
        if table_name in self.tables.keys():
            self.tables.pop(table_name)
        else:
            raise(TableNotFound(table_name))

    def create_table(self, name):
        """Create a table"""
        if not name in self.tables.keys():
            table = Tables_(str(name))
            self.tables[str(name)] = table
        else:
            print(f'Table: {name}, Already in Database')

    def save(self):
        """Save Values"""
        open(self.filename,'wb').write(base64.b64encode(pickle.dumps(self)))
        self.updated_at = datetime.now().strftime(GSTRFTIME)

    def loads(self) -> classmethod:
        """Get Stored Values"""
        if open(self.filename,'r+'):
            me = pickle.loads(base64.b64decode(open(self.filename,'rb').read()))
        else:
            me = self
        return me

    def startup(self):
        """Start And Load Database"""
        if not os.path.exists(self.filename):
            open(self.filename,'w+')
            return False
        else:
            self.__dict__ = self.loads().__dict__
            return True