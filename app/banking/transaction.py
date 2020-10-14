from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from app.dao.dbinit import DBinit


class Transaction(DBinit.Base):
    __tablename__ = 'transaction'
    id = Column('id', Integer(), primary_key=True)
    customer_id = Column('customer_id', Integer(), ForeignKey('customer.id', ondelete="cascade"))
    account_id = Column('account_id', Integer(), ForeignKey('account.id', ondelete="cascade"))
    tx_type = Column('tx_type', String(255))
    description = Column('description', String(255))
    merchant_name = Column('merchant_name', String(255))
    tx_category = Column('tx_category', String(255))
    tx_date = Column('tx_date', DateTime)
    amount = Column('amount', Float)
    created_time = Column('created_time', DateTime)

    def __init__(self, account_id, tx_type, description, merchant_name, tx_category, tx_date,
                 amount, created_time, customer_id, id=None, ):
        self.id = id
        self.account_id = account_id
        self.tx_type = tx_type
        self.description = description
        self.merchant_name = merchant_name
        self.tx_category = tx_category
        self.tx_date = tx_date
        self.amount = amount
        self.created_time = created_time
        self.customer_id = customer_id

    def __str__(self):
        return "Transaction: Id : % s , \n" \
               "tx_type % s, Description % s \n " \
               "Merchant Name % s Date % s Amount: % s" % (self.id, self.tx_type,
                                                           self.description, self.merchant_name,
                                                           self.tx_date, self.amount)
