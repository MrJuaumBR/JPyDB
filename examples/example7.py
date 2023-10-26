"""
Supported File Types:
'pydb'
'pyb'
'pyd'
'data'
'pydata'
'db'

Any Other will result in a error
"""

from JPyDB import pyDatabase

try:#With Error
    pyd = pyDatabase('database','aaaa')
except Exception as err:
    print("Error occurred: ", err)

try:# No error
    pyd = pyDatabase('database', 'pydata')
except:
    print("Unknown error.")

pyd.get_content()