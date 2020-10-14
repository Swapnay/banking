from app.banking.account import Account
from datetime import datetime
from app.dao.dbinit import DBinit
from sqlalchemy import Column, Integer, Float


class Loan(Account, DBinit.Base):
    principal = Column('principal', Float)
    loan_balance = Column('loan_balance', Float)
    term = Column('term', Integer())

    __mapper_args__ = {
        'polymorphic_identity': 'Loan'
    }

    def __init__(self, pending_deposits, routing_number_dd, routing_number_wt, interest_rate, created_time,
                 employee_id, principal, loan_balance, term, customer_id=None, id=None):
        super().__init__(0, pending_deposits, 0, 0, routing_number_dd, routing_number_wt, employee_id, 0,
                         interest_rate, created_time, customer_id, datetime(datetime.now().year,
                                                                            datetime.now().month, 25), id)
        self.principal = principal
        self.loan_balance = loan_balance
        self.term = term
        self.current_balance_to_pay = self.calculate_apr(principal, interest_rate, term)

    def __str__(self):
        return "Account: Type : Loan , \n" \
               "Current Balance to pay% s, Due on or before % s" % (self.current_balance_to_pay, self.date_due)

    '''M=P[r(1+r)^n/((1+r)^n)-1)]'''

    def calculate_apr(self, principal, annual_interest_rate, term):
        monthly_interest = annual_interest_rate / 12
        total_number_of_payments = term * 12
        monthly = principal * (monthly_interest * pow(1 + monthly_interest, total_number_of_payments)) \
                  / (pow(1 + monthly_interest, total_number_of_payments) - 1)
        return monthly
