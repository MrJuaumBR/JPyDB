from JPyDB import pyDatabase

dbh = pyDatabase('database') # Load Handler and Database

db = dbh.db() # Get Database cursor

# Create Table
db.create_table('Users')

# Add Columns
db.add_column('Users','Name',str,False)
db.add_column('Users','Age',int,False)

# Add Values
db.add_value('Users','Name',0,'A')
db.add_value('Users','Age',0,23)

db.add_value('Users','Name',1,'B')
db.add_value('Users','Age',1,27)

# Get Stored Values
dbh.get_content() # Print all values

# Get Specific Stored Value
print(db.get('Users',0)) # Print Specific ID Value

# Save Values
db.save()