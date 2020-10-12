from app.banking.account import Account
from sqlalchemy.orm import mapper, relationship


class Checking(Account):
    def __init__(self, current_balance, pending_deposits, pending_withdrawals, available_balance, routing_number_dd, routing_number_wt, over_draw_fee, created_time, employee_id):
        super().__init__(current_balance, pending_deposits, pending_withdrawals, available_balance, routing_number_dd, routing_number_wt, employee_id, id=None)
        self.over_draw_fee = over_draw_fee
        self.created_time = created_time

    '''@property
    def over_draw_fee(self):
        return self.over_draw_fee

    def over_draw_fee(self, value):
        self.over_draw_fee = value'''

    def __str__(self):
        return "Account: Type : Checking , \n" \
               "Available Balance % s, Pending Deposits % s \n " \
               "Pending withdrawals % s" % (self.available_balance, self.pending_deposits, self.pending_withdrawals)


mapper(Checking, inherits=Account, polymorphic_identity='Checking', exclude_properties={'interest_rate'})