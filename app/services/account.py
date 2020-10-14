from app.dao.accountdao import AccountDao
from app.banking.savings import Savings
from app.banking.loan import Loan
from app.banking.credit import CreditCard
from app.banking.transaction import Transaction
from app.banking.checking import Checking
from datetime import datetime
from app.dao.customerdao import CustomerDao
import random
import logging


class AccountService:
    logger = logging.getLogger('app.services.AccountService')
    account_dao = AccountDao()
    customer_dao = CustomerDao()

    def __init__(self):
        pass

    def get_account_details(self, customer_id, type):
        return self.account_dao.get_account(customer_id, type)

    def create_account_details(self, initial_amount, principal, annual_interest, emp_id,
                               customer_id):
        pass

    def update_account_details(self, account):
        self.account_dao.create_update_account(account)
        return account

    def withdraw_money(self, account, money, customer):
        try:
            logging.info("Withdraw money %s", account.customer_id)
            if account.available_balance < money:
                raise Exception("insufficient funds in account {1}".format_map(account.type))
            account.available_balance = account.available_balance - money
            account.current_balance = account.current_balance -money
            transaction = Transaction(account.id, "withdrawals", "withdrawal", "online banking",
                                      "Cash/Check withdrawal", datetime.now(), -money, datetime.now(),
                                      customer.id)
            customer.transactions.append(transaction)
            self.customer_dao.create_customer(customer)
            logging.info("Withdraw money  Successful %s", account.customer_id)
            return self.customer_dao.get_customer_by_id(customer.id)
        except Exception as ex:
            logging.error("Withdraw money error %s", ex)

    def deposit_money(self, account, money, customer):
        try:
            logging.info("Deposit money %s", account.customer_id)
            print("Deposit into account", account.type)
            logging.info("Deposit %s into  %s", money, account.type)
            account.available_balance = account.available_balance + money
            account.current_balance = account.current_balance + money
            transaction = Transaction(account.id, "Deposits", "Deposits", "online banking",
                                      "Cash/Check deposits", datetime.now(), money, datetime.now(),
                                      customer.id)
            customer.transactions.append(transaction)
            self.customer_dao.create_customer(customer)
            logging.info("Deposit money successful %s", account.customer_id)
            return self.customer_dao.get_customer_by_id(customer.id)
        except Exception as ex:
            logging.error("Deposit money error %s", ex)

    def transfer_money(self, from_account, to_account, money, customer):
        try:
            self.validate_account(from_account, to_account.type, money)
            from_account.current_balance = from_account.current_balance - money
            from_account.available_balance = from_account.available_balance - money
            to_account.current_balance = to_account.current_balance + money
            from_transaction = Transaction(from_account.id, "Withdraw", " transfer to account", to_account.type,
                                           "online banking", datetime.now(), -money, datetime.now(), customer.id)
            to_transaction = Transaction(to_account.id, "Deposit", "transfer from account ", from_account.type,
                                         "online banking", datetime.now(), money, datetime.now(), customer.id)
            self.account_dao.transfer_money(from_account, to_account, from_transaction, to_transaction, customer)
            return self.customer_dao.get_customer_by_id(from_account.customer_id)
        except Exception as ex:
            logging.error("transfer money error %s", ex)

    def validate_account(self, from_account, to_account_type, money):
        print('Transfer money from {0} to {1} amount ${2} '.format(from_account.type, to_account_type, money))
        if from_account.current_balance < money:
            raise Exception("insufficient funds in account {1}".format_map(from_account.type))


class LoanService(AccountService):
    def __init__(self):
        pass

    def create_account_details(self, initial_amount, principal, annual_interest, term, emp_id, customer):
        account = Loan(0, round(100000 * random.random()), round(100000 * random.random()), annual_interest,
                       datetime.now(), emp_id, principal, principal, term, customer.id)
        self.account_dao.create_update_account(customer, account)

    def transfer_money(self, from_account, to_account, money, customer):
        try:
            super().validate_account(from_account, to_account.type, money)
            from_account.current_balance = from_account.current_balance - money
            from_account.available_balance = from_account.available_balance - money
            to_account.current_balance_to_pay = to_account.current_balance_to_pay - money
            from_transaction = Transaction(from_account.id, "Withdraw", " transfer to account", to_account.type,
                                           "online banking", datetime.now(), -money, datetime.now(), customer.id)
            to_transaction = Transaction(to_account.id, "Deposit", "transfer  to account Loan ", from_account.type,
                                         "online banking", datetime.now(), money, datetime.now(), customer.id)
            self.account_dao.transfer_money(from_account, to_account, from_transaction, to_transaction, customer)
            return self.customer_dao.get_customer_by_id(from_account.customer_id)
        except Exception as ex:
            logging.error("transfer money error in Loan %s", ex)


class CreditService(AccountService):
    def __init__(self):
        pass

    def create_account_details(self, initial_amount, principal, annual_interest, term, emp_id, customer):
        account = CreditCard(0, 0, 0, 0, round(100000 * random.random()), round(100000 * random.random()),
                             annual_interest, 0, datetime.now(), emp_id, 0, customer.id)
        self.account_dao.create_update_account(customer, account)

    def transfer_money(self, from_account, to_account, money, customer):
        try:
            super().validate_account(from_account, to_account.type, money)
            from_account.current_balance = from_account.current_balance - money
            to_account.current_balance_to_pay = to_account.current_balance_to_pay - money
            from_transaction = Transaction(from_account.id, "Withdraw", " transfer to account", to_account.type,
                                           "online banking", datetime.now(), -money, datetime.now(), customer.id)
            to_transaction = Transaction(to_account.id, "Deposit", "transfer  to account Loan ", from_account.type,
                                         "online banking", datetime.now(), money, datetime.now(), customer.id)
            self.account_dao.transfer_money(from_account, to_account, from_transaction, to_transaction, customer)
            return self.customer_dao.get_customer_by_id(from_account.customer_id)
        except Exception as ex:
            logging.error("transfer money error credit %s", ex)


class SavingsService(AccountService):
    def __init__(self):
        pass

    def create_account_details(self, initial_amount, principal, annual_interest, term, emp_id, customer):
        account = Savings(initial_amount, 0, 0, initial_amount, round(100000 * random.random()),
                          round(100000 * random.random()), annual_interest, 50,
                          datetime.now(), emp_id, customer.id)
        self.account_dao.create_update_account(customer, account)
        return self.get_account_details(account.customer_id, account.type)


class CheckingService(AccountService):
    def __init__(self):
        pass

    def create_account_details(self, initial_amount, principal, annual_interest, term, emp_id, customer):
        account = Checking(initial_amount, 0, 0, initial_amount, round(100000 * random.random()),
                           round(100000 * random.random()), 50, annual_interest,
                           datetime.now(), emp_id, customer.id)
        self.account_dao.create_update_account(customer, account)
        return self.get_account_details(account.customer_id, account.type)
