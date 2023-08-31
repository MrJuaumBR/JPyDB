from .Handler import (Columns_,Database_,Tables_,Handler_)



class pyDatabase(Handler_):
    """Main Startup"""
    __VERSION__ = 0.2
    def __init__(self, filename="") -> Handler_:
        """Initialize, filename='' to load after init"""
        super().__init__(filename)