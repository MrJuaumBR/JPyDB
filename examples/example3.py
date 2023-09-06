from JPyDB import pyDatabase

"""
Created 0.4
"""

dbh = pyDatabase('database') # Load Handler and Database

db = dbh.db() # Get Database cursor

db.create_table('Players',(('username',str),('config',dict))) # Create a table with columns

dbh.get_content() # Get Content