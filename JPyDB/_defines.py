import pickle
import base64
import os

GSTRFTIME = "%d/%m/%Y %H:%I"
from datetime import datetime

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
                print(f'Value: {id}, Incorrect Type')
        else:
            print(f'Value: {id}, Already in Column')

    def update_value(self, id:any, value:any):
        if str(id) in self.values.keys():
            if type(value) == self.type:
                self.values[str(id)] = value
            else:
                print(f'Value: {id}, Incorrect Type')
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

    def add_column(self, name:str, type:type, null:bool):
        if not name in self.columns.keys():
            col = Columns_(name, type, null)
            self.columns[name] = col
        else:
            print(f'Column: {name}, Already in Table')

    def delete_column(self, column_name:str):
        if column_name in self.columns.keys():
            self.columns.pop(column_name)
        else:
            print(f'Column: {column_name}, Not Found in Table')

    def add_value(self, name:str, id:int, value:any):
        if name in self.columns.keys():
            col:Columns_ = self.columns[name]
            col.add_value(id, value)
        else:
            print(f'Column: {name}, Not Found in Table')

    def update_value(self, name:str, id:int, value:any):
        if name in self.columns.keys():
            col:Columns_ = self.columns[name]
            col.update_value(id, value)
        else:
            print(f'Column: {name}, Not Found in Table')

    def get_value(self, column:str, id) -> any:
        if column in self.columns.keys():
            return self.columns[column].get_value(id)
        else:
            print(f'Column: {column}, Not Found in Table')

    def get(self, id) -> any:
        g = {}
        for col in self.columns.keys():
            c:Columns_ = self.columns[col]
            if str(id) in c.values.keys():
                g[col] = c.get_value(id)
        return g

class Database_():
    def __init__(self,filename:str) -> None:
        self.filename=  "./"+str(filename)+".pydb"
        self.tables = {}

        self.created_at = datetime.now().strftime(GSTRFTIME)
        self.updated_at = ""

        self.startup()

    def add_column(self, table_name:str,name:str, type:type, null:bool):
        if table_name in self.tables.keys():
            self.tables[table_name].add_column(name, type, null)
        else:
            print(f'Table: {table_name}, Not Found in Database')

    def delete_column(self, table_name:str, column_name:str):
        if table_name in self.tables.keys():
            self.tables[table_name].delete_column(column_name)
        else:
            print(f'Table: {table_name}, Not Found in Database')

    def get(self, table_name, id) -> any:
        if table_name in self.tables.keys():
            x:Columns_ = self.tables[table_name]
            return x.get(id)
        else:
            print(f'Table: {table_name}, Not Found in Database')

    def get_value(self, table_name:str,column_name:str, id) -> any:
        if table_name in self.tables.keys():
            return self.tables[table_name].get_value(column_name, id)
        else:
            print(f'Table: {table_name}, Not Found in Database')

    def add_value(self, table_name:str,column_name:str, id:int, value:any):
        if table_name in self.tables.keys():
            self.tables[table_name].add_value(column_name, id, value)
        else:
            print(f'Table: {table_name}, Not Found in Database')
    
    def update_value(self, table_name:str,column_name:str, id:int, value:any):
        if table_name in self.tables.keys():
            self.tables[table_name].update_value(column_name, id, value)
        else:
            print(f'Table: {table_name}, Not Found in Database')

    def delete_table(self, table_name:str):
        if table_name in self.tables.keys():
            self.tables.pop(table_name)
        else:
            print(f'Table: {table_name}, Not Found in Database')

    def create_table(self, name):
        if not name in self.tables.keys():
            table = Tables_(str(name))
            self.tables[str(name)] = table
        else:
            print(f'Table: {name}, Already in Database')

    def save(self):
        open(self.filename,'wb').write(base64.b64encode(pickle.dumps(self)))
        self.updated_at = datetime.now().strftime(GSTRFTIME)

    def loads(self) -> classmethod:
        if open(self.filename,'r+'):
            me = pickle.loads(base64.b64decode(open(self.filename,'rb').read()))
        else:
            me = self
        return me

    def startup(self):
        if not os.path.exists(self.filename):
            open(self.filename,'w+')
            return False
        else:
            self.__dict__ = self.loads().__dict__
            return True