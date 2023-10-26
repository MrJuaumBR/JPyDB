"""Database error..."""
class TableNotFound(Exception):
    def __init__(self, table_name:str) -> None:
        super().__init__(table_name)
        self.message=f'Table {table_name} Not Found!'

class ColumnNotFound(Exception):
    def __init__(self, column_name:str) -> None:
        super().__init__(column_name)
        self.message=f'Column {column_name} Not Found!'

class IdNotFound(Exception):
    def __init__(self, id) -> None:
        super().__init__(id)
        self.message=f'Id: {id}, Not Found!'

"""Others error..."""
class NotExpectedReturn(Exception):
    def __init__(self,file_path) -> None:
        super().__init__(file_path)
        self.message=f'File: {file_path}, is expected a return, but not happened.'

"""Args Error..."""

class FileTypeNotExist(Exception):
    def __init__(self, fileType:str, supported:list) -> None:
        super().__init__(fileType, supported)
        self.message = f'File Type: {fileType}, is not supported! Supported: {supported}'

class IncorrectValueType(Exception):
    def __init__(self, value_id:int, value) -> None:
        super().__init__(value_id,value)
        self.message=f'Value {value_id} Type is incorrect! Value Type: {type(value)}'

class IncorrectSizeColumns(Exception):
    def __init__(self, Columns:list[str,], ExColumns:dict) -> None:
        super().__init__(Columns, ExColumns)
        self.message=f'Columns: {len(Columns)}({Columns}), is more than {len(ExColumns.keys())}({ExColumns})'

class IncorrectSizeColumnsAndValues(Exception):
    def __init__(self, columns, values) -> None:
        super().__init__(columns, values)
        self.message = f'Size of Columns({columns}) need to be the same of values({values})'

"""Class Errors"""
class ClassDictGet(Exception):
    def __init__(self, className:str) -> None:
        super().__init__(className)
        self.message = f'Class: {className}, cant get class data.'