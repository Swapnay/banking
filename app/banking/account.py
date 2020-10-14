from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey, BigInteger
from app.dao.dbinit import DBinit


class Account(DBinit.Base):
    __tablename__ = 'account'
    id = Column('id', Integer(), primary_key=True)
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
    date_due = Column('date_due', DateTime)
    current_balance_to_pay = Column('current_balance_to_pay', Float)
    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'account'
    }

    def __init__(self, current_balance, pending_deposits, pending_withdrawals,
                 available_balance, routing_number_dd, routing_number_wt,
                 employee_id, over_draw_fee, interest_rate, created_time,
                 customer_id, date_due=None, id=None):
        self.current_balance = current_balance
        self.pending_deposits = pending_deposits
        self.pending_withdrawals = pending_withdrawals
        self.available_balance = available_balance
        self.routing_number_dd = routing_number_dd
        self.routing_number_wt = routing_number_wt
        self.employee_id = employee_id
        self.customer_id = customer_id
        self.id = id
        self.over_draw_fee = over_draw_fee
        self.interest_rate = interest_rate
        self.created_time = created_time
        self.date_due = date_due