from app.banking.account import Account
from app.dao.dbinit import DBinit


class Savings(Account, DBinit.Base):
    __mapper_args__ = {
        'polymorphic_identity': 'Savings'
    }

    def __init__(self, current_balance, pending_deposits, pending_withdrawals, available_balance, routing_number_dd,
                 routing_number_wt, interest_rate, over_draw_fee, created_time, employee_id, customer_id, id=None):
        super().__init__(current_balance, pending_deposits, pending_withdrawals, available_balance, routing_number_dd,
                         routing_number_wt, employee_id, over_draw_fee, interest_rate, created_time, customer_id, id)

    def __str__(self):
        return "Account: Type : Savings , \n" \
               "Available Balance % s, Pending Deposits % s \n " \
               "Pending withdrawals % s" % (self.available_balance, self.pending_deposits, self.pending_withdrawals)
