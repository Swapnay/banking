import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
import sqlalchemy as db
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import MetaData,Table, Column, String, Integer, DateTime, Float, ForeignKey,BigInteger
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, relationship
from app.dbconfig import connection_str
'''from app.banking.account import Account
#from app.banking.customer import Customer
from app.banking.checking import Checking
from app.banking.savings import Savings
from app.banking.transaction import Transaction
from app.banking.creadit import CreditCard
from app.banking.loan import Loan
from app.banking.employee import Employee'''
from contextlib import contextmanager

class DBinit(object):

    engine = db.create_engine(connection_str, echo=True)
    Base = declarative_base(bind=engine)




    @contextmanager
    def db_session(self):

        #Session = sessionmaker(bind=DBinit.engine)
        session = scoped_session(sessionmaker(autocommit=False, autoflush=True, bind=DBinit.engine))
        try:
            yield session
            session.commit()
        except Exception as ex:
            print("Error during databse connection{}", ex)
            session.rollback()
            raise
        finally:
            session.close()



#def main():
#engine = db.create_engine(connection_str, convert_unicode=True)
'''metadata = MetaData()
customer = Table('customer', metadata, Column('id', Integer(),primary_key=True), Column('first_name', String(255)),Column('last_name', String(255)),
                 Column('email', String(255), nullable=False, unique=True ),Column('home_phone', String(255)),Column('cell_phone', String(255)),Column('address', String(255))
                 ,Column('user_id', String(255), nullable=False, unique=True),Column('password', String(255), nullable=False),Column('created_time', DateTime), Column('updated_time', DateTime)
                 , Column('employee_id', Integer(),ForeignKey('employee.id') ))
account = Table('account', metadata, Column('id', Integer(),primary_key=True), Column('customer_id', Integer(),ForeignKey('customer.id', ondelete="cascade") ),
                Column('type', String(255)), Column('current_balance', Float),  Column('pending_deposits', Float), Column('pending_withdrawals', Float),
                Column('available_balance', Float), Column('routing_number_dd', BigInteger()), Column('routing_number_wt', BigInteger()), Column('over_draw_fee', Float),
                Column('interest_rate', Float), Column('created_time', DateTime))
transaction = Table('transaction', metadata, Column('id', Integer(),primary_key=True), Column('customer_id', Integer(),ForeignKey('customer.id', ondelete="cascade")),Column('account_id', Integer(),ForeignKey('account.id', ondelete="cascade")),
                    Column('tx_type', String(255)), Column('description', String(255)),  Column('merchant_name', String(255)), Column('tx_category', String(255)),
                    Column('tx_date', DateTime), Column('amount', Float), Column('created_time', DateTime))

employee = Table('employee', metadata, Column('id', Integer(),primary_key=True), Column('first_name', String(255)),Column('last_name', String(255)),
             Column('email', String(255), nullable=False, unique=True ),Column('home_phone', String(255)),Column('cell_phone', String(255)),Column('address', String(255))
             ,Column('user_id', String(255), nullable=False, unique=True),Column('password', String(255), nullable=False),Column('created_time', DateTime), Column('updated_time', DateTime))

if not database_exists(DBinit.engine.url):
    create_database(DBinit.engine.url)
    metadata.create_all(DBinit.engine)
mapper(Customer, customer,
           properties={
               'accounts': relationship(Account, backref='customer', order_by=account.columns.id, cascade="all, delete", passive_deletes=True),
               'transactions': relationship(Transaction, backref='customer', order_by=transaction.columns.id, cascade="all, delete", passive_deletes=True)
           })'''
'''exclude_properties={'interest_rate', 'over_draw_fee'}'''
'''mapper(Account, account, polymorphic_on=account.columns.type, polymorphic_identity='account')
mapper(Checking, inherits=Account, polymorphic_identity='Checking', exclude_properties={'interest_rate'})
mapper(Savings, inherits=Account, polymorphic_identity='Savings')
mapper(Employee, employee,
      properties={
           'customers': relationship(Customer, backref='employee', order_by=employee.columns.id),
       })
mapper(Transaction, transaction)

#if __name__ == "__main__":
 #   main()'''

