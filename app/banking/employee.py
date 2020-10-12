from sqlalchemy.orm import mapper, relationship
from sqlalchemy import MetaData, Table, Column, String, Integer, DateTime, Float, ForeignKey, BigInteger
from app.banking.customer import Customer

metadata = MetaData()
employee = Table('employee', metadata, Column('id', Integer(), primary_key=True), Column('first_name', String(255)), Column('last_name', String(255)),
                 Column('email', String(255), nullable=False, unique=True), Column('home_phone', String(255)), Column('cell_phone', String(255)), Column('address', String(255))
                 , Column('user_id', String(255), nullable=False, unique=True), Column('password', String(255), nullable=False), Column('created_time', DateTime), Column('updated_time', DateTime))


class Employee(object):
    def __init__(self, first_name, last_name, email, home_phone, cell_phone, address, user_id, password, created_time, updated_time, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.home_phone = home_phone
        self.cell_phone = cell_phone
        self.address = address
        self.user_id = user_id
        self.password = password
        self.created_time = created_time
        self.updated_time = updated_time
        self.id = id

    def __str__(self):
        return "Employee: Name  % s % s, \n" \
               "UserId % s, Cell Phone % s \n " \
               "Email % s, Home Phone % s \n" \
               "Address % s" % (self.first_name, self.last_name, self.user_id, self.cell_phone, self.email, self.home_phone, self.address)


mapper(Employee, employee,
 properties={
   'customers': relationship(Customer, backref='employee', order_by=employee.columns.id),
})
