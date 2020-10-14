from app.banking.account import Account
from app.dao.dbinit import DBinit


class Checking(Account, DBinit.Base):
    __mapper_args__ = {
        'polymorphic_identity': 'Checking'
    }

    def __init__(self, current_balance, pending_deposits, pending_withdrawals, available_balance, routing_number_dd, routing_number_wt, over_draw_fee, interest_rate, created_time, employee_id,
                 customer_id):
        super().__init__(current_balance, pending_deposits, pending_withdrawals, available_balance, routing_number_dd, routing_number_wt, employee_id, over_draw_fee, interest_rate, created_time,
                         customer_id)

    def __str__(self):
        return "Account: Type : Checking , \n" \
               "Available Balance % s, Pending Deposits % s \n " \
               "Pending withdrawals % s" % (self.available_balance, self.pending_deposits, self.pending_withdrawals)
