from sqlalchemy.orm import mapper, relationship
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import MetaData, Table, Column, String, Integer, DateTime, Float, ForeignKey, BigInteger
from app.dao.dbinit import DBinit


metadata = MetaData()
account = Table('account', metadata, Column('id', Integer(), primary_key=True), Column('customer_id', Integer(), ForeignKey('customer.id', ondelete="cascade")),
                Column('type', String(255)), Column('current_balance', Float), Column('pending_deposits', Float), Column('pending_withdrawals', Float),
                Column('available_balance', Float), Column('routing_number_dd', BigInteger()), Column('routing_number_wt', BigInteger()), Column('over_draw_fee', Float),
                Column('interest_rate', Float), Column('created_time', DateTime))


class Account(DBinit.Base):
    __tablename__ = 'account'
    id= Column('id', Integer(), primary_key=True)
    customer_id = Column('customer_id', Integer(), ForeignKey('customer.id', ondelete="cascade"))
    type = Column('type', String(255))
    current_balance = Column('current_balance', Float)
    pending_deposits = Column('pending_deposits', Float)
    pending_withdrawals = Column('pending_withdrawals', Float)
    available_balance = Column('available_balance', Float)
    routing_number_dd = Column('routing_number_dd', BigInteger())
    routing_number_wt = Column('routing_number_wt', BigInteger())
    over_draw_fee = Column('over_draw_fee', Float)
    interest_rate = Column('interest_rate', Float)
    created_time = Column('created_time', DateTime)
    def __init__(self, current_balance, pending_deposits, pending_withdrawals, available_balance, routing_number_dd, routing_number_wt, employee_id, id=None):
        self.current_balance = current_balance
        self.pending_deposits = pending_deposits
        self.pending_withdrawals = pending_withdrawals
        self.available_balance = available_balance
        self.routing_number_dd = routing_number_dd
        self.routing_number_wt = routing_number_wt
        self.employee_id = employee_id
        self.id = id

    @property
    def current_balance(self):
        return self.current_balance

    def current_balance(self, value):
        self.current_balance = value

    @property
    def pending_deposits(self):
        return self.pending_deposits

    def pending_deposits(self, value):
        self.pending_deposits = value

    @property
    def pending_withdrawals(self):
        return self.pending_withdrawals

    @property
    def available_balance(self):
        return self.available_balance

    def available_balance(self, value):
        self.available_balance = value

    @property
    def routing_number_dd(self):
        return self.routing_number_dd

    def routing_number_dd(self, value):
        self.routing_number_dd = value

    @property
    def routing_number_wt(self):
        return self.routing_number_wt

    def routing_number_wt(self, value):
        self.routing_number_wt = value


mapper(Account, account, polymorphic_on=account.columns.type, polymorphic_identity='account')
