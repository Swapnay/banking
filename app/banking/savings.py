from app.banking.account import Account
from sqlalchemy.orm import mapper, relationship


class Savings(Account):
    def __init__(self, current_balance, pending_deposits, pending_withdrawals, available_balance, routing_number_dd, routing_number_wt, interest_rate, over_draw_fee, created_time):
        super().__init__(current_balance, pending_withdrawals, pending_deposits, available_balance, routing_number_dd, routing_number_wt)
        self.over_draw_fee = over_draw_fee
        self.interest_rate = interest_rate
        self.created_time = created_time

    def __str__(self):
        return "Account: Type : Savings , \n" \
               "Available Balance % s, Pending Deposits % s \n " \
               "Pending withdrawals % s" % (self.available_balance, self.pending_deposits, self.pending_withdrawals)


mapper(Savings, inherits=Account, polymorphic_identity='Savings')
