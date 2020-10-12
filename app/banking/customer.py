from app.banking.account import Account,account
from app.banking.transaction import Transaction,transaction
from sqlalchemy.orm import mapper, relationship
from sqlalchemy import MetaData,Table, Column, String, Integer, DateTime, Float, ForeignKey,BigInteger

metadata = MetaData()
customer = Table('customer', metadata, Column('id', Integer(),primary_key=True), Column('first_name', String(255)),Column('last_name', String(255)),
                 Column('email', String(255), nullable=False, unique=True ),Column('home_phone', String(255)),Column('cell_phone', String(255)),Column('address', String(255))
                 ,Column('user_id', String(255), nullable=False, unique=True),Column('password', String(255), nullable=False),Column('created_time', DateTime), Column('updated_time', DateTime)
                 , Column('employee_id', Integer(),ForeignKey('employee.id') ))
class Customer(object):

    def __init__(self, first_name, last_name, email, home_phone, cell_phone, address, user_id, password, created_time, updated_time, employee_id, id=None):
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
        self.employee_id = employee_id
        self.id=id
       # self.accounts = relationship(Account, backref='customer', order_by= account.columns.id, cascade="all, delete", passive_deletes=True)
        #self.transactions = relationship(Transaction, backref='customer', order_by= transaction.columns.id, cascade="all, delete", passive_deletes=True)


    def __str__(self):
        return "Customer: Name  % s % s, \n" \
               "UserId % s, Cell Phone % s \n " \
               "Email % s, Home Phone % s \n" \
               "Address % s employee %s" % (self.first_name, self.last_name, self.user_id, self.cell_phone, self.email, self.home_phone, self.address, self.employee_id)

mapper(Customer, customer,
       properties={
           'accounts': relationship(Account, backref='customer', order_by=account.columns.id, cascade="all, delete", passive_deletes=True),
           'transactions': relationship(Transaction, backref='customer', order_by=transaction.columns.id, cascade="all, delete", passive_deletes=True)
       })