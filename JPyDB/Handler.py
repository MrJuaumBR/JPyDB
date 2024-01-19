from ._defines import *

class Handler_():
    """Handler, load content and others"""
    VERSION = 0
    def __init__(self,filename, fileType:str="pydb"):
        self.database:Database_ = Database_(filename, fileType)

        self.encryption = ["b64","pickle"]

        self.VERSION = self.database.VERSION

    def db(self) -> Database_:
        return self.database
    
    def get_db_size(self) -> float:
        return self.database.get_db_size()

    def deleteDatabase(self):
        """Delete Database"""
        self.database._deleteDb()

    def save(self):
        self.database.save()

    def GetSheet(self, output:str):
        """
        GetSheet is a method that takes a string parameter called output and returns nothing.

        Parameters:
            - output (str): The output string parameter.

        Create:
            - .xls file
        """
        from .sheeting import output as out
        out(output, self)

    def get_content(self):
        d = self.database
        print("Content:")
        for table in d.tables.items():
            print("|_Table: ",table[0])
            for column in table[1].columns.items():
                print("  |_Column: ", column[0])
                for value in column[1].values.items():
                    print("    |_Value: ", value[0]," | ",value[1])