from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey

engine = create_engine('sqlite:///:memory:', echo=True)

meta = MetaData()

# Define table "students"
students = Table(
    'students', meta, 
    Column('id', Integer, primary_key = True), 
    Column('name', String), 
    Column('lastname', String),
)

# Define table "adresses"
addresses = Table(
    'addresses', meta, 
    Column('id', Integer, primary_key = True), 
    Column('email_address', String), 
    Column("student_id", None, ForeignKey("students.id"))
)

meta.create_all(engine)

ins = students.insert().values(id="1", name="Jack", lastname="Johnson")

conn = engine.connect()
result = conn.execute(ins)

values = [
    {'student_id': 1, 'email_address' : 'jack@yahoo.com'},
    {'student_id': 1, 'email_address' : 'jack@msn.com'}
]

conn.execute(addresses.insert(), values)

from sqlalchemy.sql import text

# Create a statement 
stmt = text("SELECT students.id, addresses.id, students.name, addresses.email_address FROM students "
            "JOIN addresses ON students.id=addresses.student_id "
            "WHERE students.id = 1")

result = conn.execute(stmt)

result.fetchall()