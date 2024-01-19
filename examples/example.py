from JPyDB import pyDatabase

"""
Created 0.2
Updated to 0.8
"""

dbh = pyDatabase('database') # Load Handler and Database

db = dbh.db() # Get Database cursor

# Create Table
db.create_table('Users')
db.create_table('Something',[('Foo',str),('Bar',int)])

# Add Columns
db.add_column('Users','Name',str,False)
db.add_column('Users','Age',int,False)

# Add Values
db.add_values('Users',db.tables['Users'].columns.keys(),['User 1',23],0) # Add multiples values
db.add_values('Users',['Name','Age'],['User 2',24],1) # Other form
db.add_values('Users',['Name','Age'],['User 3',32],2)

db.add_values('Something',['Foo','Bar'],['Foo 1',1],0)
db.add_values('Something',['Foo','Bar'],['Foo 2',2],1)
db.add_values('Something',['Foo','Bar'],['Foo 3',3],2)

dbh.get_content() # Get all values

#print(db.get('Users',0)) # Get all values from a Id

# Save Values
db.save()

# Delete Database
#dbh.deleteDatabase()
dbh.GetSheet('output')