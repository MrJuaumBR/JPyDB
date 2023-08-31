from .Handler import (Columns_,Database_,Tables_,Handler_)

class pyDatabase(Handler_):
    __VERSION__ = 0.2
    def __init__(self, filename) -> None:
        super().__init__(filename)