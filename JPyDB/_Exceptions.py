"""Database error..."""
class TableNotFound(Exception):
    def __init__(self, table_name:str) -> None:
        super().__init__(table_name)
        self.message=f'Table {table_name} Not Found!'

class ColumnNotFound(Exception):
    def __init__(self, column_name:str) -> None:
        super().__init__(column_name)
        self.message=f'Column {column_name} Not Found!'

"""Args Error..."""

class ValueTypeIncorrect(Exception):
    def __init__(self, value_id:int) -> None:
        super().__init__(value_id)
        self.message=f'Value {value_id} Type is incorrect!'

class IncorrectSizeColumnsAndValues(Exception):
    def __init__(self, columns, values) -> None:
        super().__init__(columns, values)
        self.message = f'Size of Columns({columns}) need to be the same of values({values})'