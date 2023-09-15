from JPyDB import pyDatabase

DB = pyDatabase('database')

DB.database.create_table('Users',[('username',str,False),('email',str,False)])

DB.database.add_values('Users',['username','email'],['teste','teste@gmail.com'],0)
DB.database.add_values('Users',['username','email'],['teste2','teste2@gmail.com'],1)


#DB.database.delete_all('Users') # Delete all
#DB.database.delete_values('Users',2) # delete all by Id
#DB.database.tables['Users'].delete_value('email',1) # Delete only a value

DB.save()

DB.get_content()