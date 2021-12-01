from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.sql import text
from sqlalchemy.sql import select
engine = create_engine('sqlite:///office.db', echo=True)
meta = MetaData()
conn = engine.connect()
employee = Table(
   'employee', meta, 
   Column('id', Integer, primary_key = True), 
   Column('dept_id', Integer, ForeignKey('departments.id')),
   Column('name', String, nullable= False), 
   Column('salary', Integer,default=1000), 
)

departments = Table(
   'departments', meta, 
   Column('id', Integer, primary_key = True), 
  
   Column('name', String), 
   Column('m_id', Integer, ForeignKey('employee.id')))

# meta.create_all(engine)

# conn.execute(employee.insert(), [
#    {'id': 1,'dept_id':1,'name':'Ravi', 'salary': 9000},
#    {'id': 2,'dept_id':2,'name':'Rajiv', 'salary' : 15000},
#    {'id': 3,'dept_id':2,'name':'Komal','salary' : 1000},
#    {'id': 4,'dept_id':2,'name':'Abdul','salary' : 2000},
#    {'id': 5,'dept_id':1,'name':'Priya','salary' : 5000},
# ])



# conn.execute(departments.insert(), [
#    { 'id':1,'name':'Accounts', 'm_id' : 1},
#    { 'id':2,'name':'Computer', 'm_id': 2},
   
# ])

#Selecting employees using dept_id
# s = select([employee,departments]).where(employee.c.dept_id == departments.c.id , departments.c.id==2 )
# result = conn.execute(s)

# for row in result:
#    print (row)

# s = select([employee,departments]).where(employee.c.dept_id == departments.c.id , departments.c.id==1 )
# result = conn.execute(s)

# for row in result:
#    print (row)

#Selecting from employee using manager id

s = select([employee,departments]).where(employee.c.id == departments.c.m_id)
result = conn.execute(s)

for row in result:
   print (row)


