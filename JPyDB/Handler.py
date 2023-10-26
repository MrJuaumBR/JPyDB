from ._defines import *

class Handler_():
    """Handler, load content and others"""
    def __init__(self,filename, fileType:str="pydb"):
        self.database:Database_ = Database_(filename, fileType)

        self.encryption = ["b64","pickle"]

    def db(self) -> Database_:
        return self.database

    def deleteDatabase(self):
        """Delete Database"""
        self.database._deleteDb()

    def save(self):
        self.database.save()

    def get_content(self):
        d = self.database
        print("Content:")
        for table in d.tables.items():
            print("|_Table: ",table[0])
            for column in table[1].columns.items():
                print("  |_Column: ", column[0])
                for value in column[1].values.items():
                    print("    |_Value: ", value[0]," | ",value[1])