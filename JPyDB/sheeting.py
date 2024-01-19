

import xlwt
import os
from ._defines import Columns_
from .Handler import Handler_

def output(filename,Handler:Handler_):
    """
    Output return a xls file
    Parameters:
        - filename (str): The exit filename e.g. 'output'
        - DB (Handler): The Database Object
    """
    if os.path.exists(filename+'.xls'):
        os.remove(filename+'.xls')
    book = xlwt.Workbook()
    DB = Handler.db()
    for x,table in enumerate(DB.tables.keys()):
        sheet = book.add_sheet(str(table))
        sheet.write(0,0,'Id')

        
        for y,column in enumerate(DB.tables[table].columns.keys()):
            Already = []    
            sheet.write(0,1+y,label=f"{column}")
            Col = DB.tables[table].columns[column]
            for z,value in enumerate(Col.values.keys()):
                if not (value in Already):
                    Already.append(value)
                    try:
                        sheet.write(z+1,1+y,label=Col.values[value])
                    except Exception as err:
                        print(err, f'\t{value}')
            for id in Already:
                try:
                    sheet.write(int(id)+1,0,label=id)
                except Exception as err:
                    pass
            
    
    
    # Some Data
    sh = book.add_sheet("Data")
    sh.write(0,0,f'Created with: JPyDB(Ver: {DB.VERSION})')
    sh.write(1,0,f'Created at: {DB.created_at}')
    
    # Counters
    sh.write(2,0,f'Number of tables:')
    sh.write(2,1,f'{len(DB.tables)}')

    # Misc
    sh.write(3,0,f'Supported types: ')
    sh.write(3,1,f'{DB.DB_TYPES}')

    sh.write(4,0,f'Encryption:')
    sh.write(4,1,f'{Handler.encryption}')

    book.save(filename+'.xls')