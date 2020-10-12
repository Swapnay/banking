from app.banking.account import Account


class CreditCard(Account):
    def __init__(self, current_balance, pending_deposits, pending_withdrawals, available_balance, routing_number_dd, routing_number_wt, interest_rate, over_draw_fee, created_time, employee_id,
                 current_balance_to_pay, date_due, id=None):
        super().__init__(current_balance, pending_withdrawals, pending_deposits, available_balance, routing_number_dd, routing_number_wt, employee_id, id)
        self.over_draw_fee = over_draw_fee
        self.interest_rate = interest_rate
        self.created_time = created_time
        self.current_balance_to_pay = current_balance_to_pay
        self.date_due = date_due

    def __str__(self):
        return "Account: Type : CreditCard , \n" \
               "Current Balance to pay% s, date_due Deposits % s" % (self.current_balance_to_pay, self.date_due)
