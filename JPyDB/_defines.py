import pickle
import base64
import os
from inspect import isclass

GSTRFTIME = "%d/%m/%Y %H:%I:%S"
from datetime import datetime

from ._Exceptions import (TableNotFound, ColumnNotFound, IncorrectValueType, IncorrectSizeColumnsAndValues, NotExpectedReturn, IdNotFound, IncorrectSizeColumns, ClassDictGet, FileTypeNotExist)

class Columns_():
    def __init__(self,name:str, type:type, not_null:bool) -> None:
        self.column_name = name
        self.type = type
        self.not_null = not_null

        self.values = {}

    def findByText(self, text) -> int or str:
        for key in self.values.keys():
            if str(self.values[key]).lower() == str(text).lower():
                return key
        return None

    def add_value(self,id:any=None, value:any=None):
        if id in [None,"None"," "]:
            id = len(self.values.keys())
        if not str(id) in self.values.keys():
            if type(value) == self.type:
                self.values[str(id)] = value
            elif self.type == any:
                if isclass(value):
                    # Class or instance
                    v = None
                    try:
                        v = value.__dict__
                    except:
                        v = None
                    if v:
                        self.values[str(id)] = v
                    else:
                        raise(ClassDictGet(str(type(value).__name__)))
                else:
                    self.values[str(id)] = value
            else:
                raise(IncorrectValueType(str(id),value))
        else:
            print(f'Value: {id}, Already in Column')

    def update_value(self, id:any, value:any):
        if str(id) in self.values.keys():
            if type(value) == self.type:
                self.values[str(id)] = value
            else:
                raise(IncorrectValueType(str(id)))
        else:
            raise(IdNotFound(str(id)))

    def delete_value(self, id:any):
        if str(id) in self.values.keys():
            del self.values[str(id)]
        else:
            raise(IdNotFound(str(id)))

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

    def findByText(self,column:str,text:str):
        x = None
        if self.columns[column]:
            id = self.columns[column].findByText(text)
            x = self.get(id)
        else:
            raise(ColumnNotFound(column))
        return x

    def ids_count(self) -> int:
        x = len(self.columns[next(iter(self.columns))].values)
        return x

    def get_all(self) -> list:
        l = []
        for c,column in enumerate(self.columns.keys()):
            for x,value in enumerate(self.columns[column].values.keys()):
                if not self.get(value) in l:
                    l.append(self.get(value))
                if x >= self.ids_count():
                    break
            if c >= 0:
                break
        return l

    def add_column(self, column_name:str, type:type, null:bool=False):
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

    def delete_value(self, column_name:str, id:int=None):
        if column_name in self.columns.keys():
            col:Columns_ = self.columns[column_name]
            col.delete_value(id)
        else:
            raise(ColumnNotFound(column_name))

    def delete_values(self, columns_names:list[str,], id:int=None):
        if len(columns_names) <= len(self.columns.keys()):
            for col in columns_names:
                self.delete_value(col, id)
        else:
            raise(IncorrectSizeColumns(columns_names,self.columns))

    def add_value(self, column_name:str, id:int=None, value:any=None):
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

    def get(self, id) -> dict:
        g = {}
        for col in self.columns.keys():
            c:Columns_ = self.columns[col]
            if str(id) in c.values.keys():
                g[col] = c.get_value(id)

        g['id'] = id
        return g

class Database_():
    """Database Cursor and controller"""
    DB_TYPES = ['pydb', 'pyb', 'pyd','data','pydata','db']
    def __init__(self,filename:str, fileType="pydb") -> None:
        if not (fileType in self.DB_TYPES):
            raise(FileTypeNotExist(fileType, self.DB_TYPES))
        self.CommonLoad = False
        if not filename in ['',' ', None]:
            self.CommonLoad = True
            self.filename=  "./"+str(filename)+f".{fileType}"
        self.tables = {}

        self.created_at = datetime.now().strftime(GSTRFTIME)
        self.updated_at = ""

        if self.CommonLoad:
            self.startup()

    def _deleteDb(self):
        if self.CommonLoad and self.filename:
            os.remove(self.filename)

    def findByText(self, table:str,column:str,text:str) -> dict:
        x = None
        if self.tables[table]:
            x = self.tables[table].findByText(column,text)
        else:
            raise(TableNotFound(table))
        return x

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

    def get_all(self, table_name) -> list[dict,]:
        if table_name in self.tables:
            l = self.tables[table_name].get_all()
        else:
            raise(TableNotFound(table_name))
        return l

    def get(self, table_name, id) -> dict:
        """Get all values by id"""
        if table_name in self.tables.keys():
            x:Tables_ = self.tables[table_name]
            return x.get(id)
        else:
            raise(TableNotFound(table_name))

    def get_value(self, table_name:str,column_name:str, id) -> any:
        """Get a value in a Table & Column"""
        if table_name in self.tables.keys():
            return self.tables[table_name].get_value(column_name, id)
        else:
            raise(TableNotFound(table_name))

    def add_value(self, table_name:str,column_name:str, id:int=None, value:any=None):
        """Add a value in a Table & Column"""
        if table_name in self.tables.keys():
            self.tables[table_name].add_value(column_name, id, value)
        else:
            raise(TableNotFound(table_name))
    
    def add_values(self, table_name:str,columns:list or tuple,values:list or tuple,id:int=None):
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

    def delete_values(self, table_name:str, id:int,columns:list[str,]=[]):
        if self.tables[table_name]:
            table:Tables_=self.tables[table_name]
            if len(columns) <= 0:
                columns = []
                for col in table.columns.keys():
                    columns.append(col)
            table.delete_values(columns,id)
        else:
            raise(ColumnNotFound(table_name))

    def delete_all(self, table_name:str):
        if table_name in self.tables.keys():
            for id in range(self.tables[table_name].ids_count()):
                self.delete_values(table_name,id)
        else:
            raise(TableNotFound(table_name))

    def delete_table(self, table_name:str):
        """Delete a table"""
        if table_name in self.tables.keys():
            self.tables.pop(table_name)
        else:
            raise(TableNotFound(table_name))

    def create_table(self, name, columns=()):
        """Create a table"""
        if not name in self.tables.keys():
            table = Tables_(str(name))
            self.tables[str(name)] = table
            if columns and columns != ():
                for column in columns:
                    if len(column) == 3:
                        not_null = column[2]
                    else:
                        not_null = False
                    table.add_column(column[0],column[1],not_null)
        else:
            print(f'Table: {name}, Already in Database')

    def save(self):
        """Save Values"""
        self.updated_at = datetime.now().strftime(GSTRFTIME)
        open(self.filename,'wb').write(base64.b64encode(pickle.dumps(self)))

    def loads(self) -> classmethod:
        """Get Stored Values"""
        if not open(self.filename,'r+').read() in [' ','',None,"None"]:
            me = pickle.loads(base64.b64decode(open(self.filename,'rb').read()))
        else:
            me = self
        return me

    def startup(self):
        """Start And Load Database"""
        if not os.path.exists(self.filename):
            open(self.filename,'w+')
            return False
        elif os.path.exists(self.filename):
            self.__dict__ = self.loads().__dict__
            return True
        raise(NotExpectedReturn(__file__))