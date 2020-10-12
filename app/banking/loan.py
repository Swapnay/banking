from app.banking.account import Account
from datetime import datetime
class Loan(Account):
    def __init__(self, pending_deposits, routing_number_dd, routing_number_wt, interest_rate, created_time, employee_id, principal, loan_balance,term,
                  date_due, customer_id =None, id=None):
        super().__init__(0, 0, pending_deposits, 0, routing_number_dd, routing_number_wt, employee_id, id)
        self.interest_rate = interest_rate
        self.created_time = created_time
        self.date_due = date_due
        self.principal = principal
        self.employee_id = employee_id
        self.loan_balance = loan_balance
        self.term = term
        self.current_balance_to_pay = self.calculate_apr(principal, interest_rate, term)
        self.date_due = datetime(datetime.now().year, datetime.now().month, 25)
        self.customer_id = customer_id


    def __str__(self):
        return "Account: Type : CreditCard , \n" \
               "Current Balance to pay% s, date_due Deposits % s" % (self.current_balance_to_pay, self.date_due)


    '''M=P[r(1+r)^n/((1+r)^n)-1)]'''
    def calculate_apr(self, principal, annual_interest_rate, term):
        monthly_interest = annual_interest_rate/12
        total_number_of_payments = term *12
        monthly = principal*(monthly_interest* pow(1+monthly_interest,total_number_of_payments))/(pow(1+monthly_interest,total_number_of_payments)-1)
        return monthly
