from app.banking.account import Account
from app.banking.transaction import Transaction
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from app.dao.dbinit import DBinit


class Customer(DBinit.Base):
    __tablename__ = 'customer'
    id = Column('id', Integer(), primary_key=True)
    first_name = Column('first_name', String(255), nullable=False)
    last_name = Column('last_name', String(255), nullable=False)
    email = Column('email', String(255), nullable=False, unique=True)
    home_phone = Column('home_phone', String(255))
    cell_phone = Column('cell_phone', String(255))
    address = Column('address', String(255), nullable=False)
    user_id = Column('user_id', String(255), nullable=False, unique=True)
    password = Column('password', String(255), nullable=False)
    created_time = Column('created_time', DateTime)
    updated_time = Column('updated_time', DateTime)
    employee_id = Column('employee_id', Integer(), ForeignKey('employee.id'))
    accounts = relationship(Account, backref='customer', order_by=Account.id, cascade="all, delete", passive_deletes=True, lazy='joined')
    transactions = relationship(Transaction, backref='customer', order_by=Transaction.id, cascade="all, delete", passive_deletes=True, lazy='joined')

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
        self.id = id

    def __str__(self):
        return "Customer: Name  % s % s, \n" \
               "UserId % s, Cell Phone % s \n " \
               "Email % s, Home Phone % s \n" \
               "Address % s employee %s" % (self.first_name, self.last_name, self.user_id, self.cell_phone, self.email, self.home_phone, self.address, self.employee_id)
