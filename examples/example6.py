from JPyDB import pyDatabase

pyb = pyDatabase('test')
db = pyb.database

db.create_table('Users', [('username',str),('email',str),('data',any)])

# Any can be used as any type.
#db.add_values('Users', ['username','email','data'],['User 1','teste@gmail.com','Some Data here'])

# For Store Class, use Dict
class MyClass():
    def __init__(self):
        self.cos = 'something'
        self.number = 1
        self.h = 1/100

MyClassData = MyClass()

# To Load
MyClassData.__dict__ = db.get('Users', 0)['data']

#db.add_values('Users', ['username','email','data'],['User 2', 'teste2@gmail.com', MyClassData.__dict__])

db.save()
pyb.get_content()