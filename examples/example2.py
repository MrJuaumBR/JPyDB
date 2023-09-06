from JPyDB import pyDatabase

"""
Created 0.3

Update Example
"""

dbh = pyDatabase('database') # Load Handler and Database

db = dbh.db() # Get Database cursor


db.update_value('Users','Name',0,'User 1')
print(db.get('Users',0))
# Update for 0
db.update_value('Users','Name',0,'User 0')
print(db.get('Users',0))

# Save Values
db.save()