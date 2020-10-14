from app.banking.account import Account
from app.dao.dbinit import DBinit


class CreditCard(Account, DBinit.Base):
    __mapper_args__ = {
        'polymorphic_identity': 'Credit'
    }

    def __init__(self, current_balance, pending_deposits, pending_withdrawals, available_balance, routing_number_dd, routing_number_wt, interest_rate, over_draw_fee, created_time, employee_id,
                 customer_id, current_balance_to_pay, date_due, id=None):
        super().__init__(current_balance, pending_deposits, pending_withdrawals, available_balance, routing_number_dd, routing_number_wt, employee_id, over_draw_fee, interest_rate, created_time,
                         customer_id, date_due, id)
        self.current_balance_to_pay = current_balance_to_pay

    def __str__(self):
        return "Account: Type : CreditCard , \n" \
               "Current Balance to pay% s, date_due Deposits % s" % (self.current_balance_to_pay, self.date_due)
