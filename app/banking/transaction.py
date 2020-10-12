from sqlalchemy.orm import mapper, relationship
from sqlalchemy import MetaData,Table, Column, String, Integer, DateTime, Float, ForeignKey,BigInteger
metadata = MetaData()
transaction = Table('transaction', metadata, Column('id', Integer(),primary_key=True), Column('customer_id', Integer(),ForeignKey('customer.id', ondelete="cascade")),Column('account_id', Integer(),ForeignKey('account.id', ondelete="cascade")),
                    Column('tx_type', String(255)), Column('description', String(255)),  Column('merchant_name', String(255)), Column('tx_category', String(255)),
                    Column('tx_date', DateTime), Column('amount', Float), Column('created_time', DateTime))

class Transaction(object):
    def __init__(self,  account_id, tx_type, description, merchant_name, tx_category, tx_date , amount, created_time, id=None,):
        self.id = id
        self.account_id = account_id
        self.tx_type = tx_type
        self.description = description
        self.merchant_name = merchant_name
        self.tx_category = tx_category
        self.tx_date = tx_date
        self.amount = amount
        self.created_time = created_time

    def __str__(self):
        return "Transaction: Id : % s , \n" \
               "tx_type % s, Description % s \n " \
               "Merchant Name % s Date % s Amount: % s" % (self.id, self.tx_type, self.description, self.merchant_name,self.tx_date, self.amount)



    ''' @property
        def tx_type(self):
            return self.tx_type
    
        def tx_type(self, value):
            self.tx_type = value
    
        @property
        def description(self):
            return self.description
    
        def description(self, value):
            self.description = value
    
        @property
        def merchant_name(self):
            return self.merchant_name
    
        def merchant_name(self, value):
            self.merchant_name = value
    
        @property
        def tx_date(self):
            return self.tx_date
    
        def tx_date(self, value):
            self.tx_date = value
    
        @property
        def tx_category(self):
            return self.tx_category
    
        def tx_category(self, value):
            self.tx_category = value'''