from .Handler import (Columns_,Database_,Tables_,Handler_)

import webbrowser

"""
DISCORD:    https://discord.gg/fb84sHDX7R
YOUTUBE:    https://www.youtube.com/channel/UClcAmcdF0OvAOEgiKr5NgYQ
GITHUB :    https://github.com/MrJuaumBR/JPyDB



DESCRIPTION:
This is a package for Python 3.x, Developed in Brazil, started in: 29/08/23

Developer: MrJuaum//MrPotato

This package, will be able to create databases with a new store system!

How This Work?
- Simple, we compact all the data into a 'pickle' object
and we store in a *.pydb file using base64

Encrypting:
Currently only Pickle and base64
But i(MrJuaum) Want to add a new layer of encryption: pyEncrypt(https://mrjuaumbr.github.io/data/pyEncrypt.py)

How i can visualize Database?
Simple: pyEncrypt.get_content() will return all values
or: "/examples/webviewer/dataviewer.py" this will require flask, and will show values more easily

Thanks for all!
"""


# Define masked
class Columns(Columns_):
    def __init__(self, name: str, type: type, not_null: bool) -> Columns_:
        super().__init__(name, type, not_null)

class Tables(Tables_):
    def __init__(self, table_name: str) -> Tables_:
        super().__init__(table_name)

class Database(Database_):
    def __init__(self, filename: str) -> Database_:
        super().__init__(filename)

# Define Masked for Handler
class pyDatabase(Handler_):
    """Main Startup"""
    __VERSION__ = 0.7
    def __init__(self, filename="", fileType:str="pydb") -> Handler_:
        """Initialize, filename='' to load after init"""
        super().__init__(filename, fileType)

    def TESTPYPI(self):
        webbrowser.open("https://test.pypi.org/project/JPyDB/")

    def GITHUB(self):
        webbrowser.open("https://github.com/MrJuaumBR/JPyDB")

    def YOUTUBE(self):
        webbrowser.open("https://www.youtube.com/channel/UClcAmcdF0OvAOEgiKr5NgYQ")

    def DISCORD(self):
        webbrowser.open("https://discord.gg/fb84sHDX7R")