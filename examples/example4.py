from JPyDB import pyDatabase

"""
Created 0.5
"""

# Init Module
dbh = pyDatabase('database')

# Define Database Cursor
db = dbh.database

# Create Table with new Options
db.create_table('Users',[('username',str),('avatar_url',str),('object',dict)])

# Example Dict
example = {}

# Add Values
db.add_values('Users',['username','avatar_url','object'],['User 0','https://google.com',example])
db.add_values('Users',['username','avatar_url','object'],['User 1','https://youtube.com',example])
db.add_values('Users',['username','avatar_url','object'],['User 2','https://gmail.com',example])

# Save
db.save()

# Get all from a specific Table
print(db.get_all('Users'))