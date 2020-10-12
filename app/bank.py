import sys
import os

PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from app.banking.customer import Customer
from app.banking.transaction import Transaction
from app.banking.checking import Checking
from app.banking.savings import Savings
from app.dao.db import DbManager
from datetime import datetime
import logging
import random


class BankingManager(object):
    logger = logging.getLogger('banking.bank.BankingManager')

    def __init__(self):
        pass


db_manager = DbManager()


def main():
    #db_manager = DbManager()
    print("Enter a choice ")
    choice = int(input("1.Employee Login 2. Customer Login 1/2?"))
    logging.info("Entered Choice %s", choice)
    if choice == 1:
        user_id = input("Enter UserID")
        password = input("Enter Password")
        try:
            employee = db_manager.get_employee( user_id, password)
            if employee is None:
                print("Incorrect user id or password ", user_id)
                return
        except Exception as ex:
            print("Incorrect user id or password ", ex)
            logging.error("Incorrect user id or password for user %s %s", user_id, ex)
            return
        choice = input("Create Customer Y/N?")
        if choice.lower() == 'y':
            customer = create_customer(employee.id)
        print("Customer created successfully. Exiting the application")
        return

    else:
        user_id = input("Enter UserID")
        password = input("Enter Password")
        try:
            customer = db_manager.get_customer(user_id, password)
            if customer is None:
                print("Incorrect user id or password ", user_id)
                return
        except:
            print("Incorrect user id or password ", user_id)
            logging.error("Incorrect user id or password for user %s", user_id)
            return
    logging.info("Customer Details %s", customer)
    while True:
        print("What would you like to do now?")
        print("1.Logout 2.Check profile 3.Withdraw Money 4.Deposit")
        choice = int(input("Enter a choice between 1-4"))
        if choice == 1:
            logging.info("Log out")
            print("Logging out..")
            break
        elif choice == 2:
            logging.info("Display Profile")
            try:
                print_customer_details(customer)
            except Exception as e:
                logging.error("Error while displaying profile details %s", e)
                print("Error while displaying profile details ", e)
                break
        elif choice == 3:
            try:
                withdraw_money(customer)
            except Exception as e:
                logging.error("Error while withdraw money %s", e)
                print("Error while withdraw money ", e)
                break
        else:
            try:
                deposit_money(customer)
            except Exception as e:
                logging.error("Error while deposit money %s", e)
                print("Error while deposit money ", e)
                break


def create_customer(employee_id):
    print("Creating Account")
    first_name = input("Enter First Name")
    last_name = input("Enter Last Name")
    email = input("Email")
    home_phone = input("Home Phone")
    cell_phone = input("Cell Phone")
    address = input("Address")
    userid = input("UserId")
    password = input("Password")
    customer = Customer(first_name, last_name, email, home_phone, cell_phone, address, userid, password, datetime.now(), datetime.now(), employee_id)
    customer.accounts.append(create_account("Checking"))
    savings = input("Would you like to open a Savings account ? Y/N")
    if savings.lower() == 'y':
        customer.accounts.append(create_account("Savings"))
        db_manager.create_customer(customer)
    return db_manager.get_user(userid, password)


def print_customer_details(customer):
    print("Customer Details:")
    print(customer)
    for account in customer.accounts:
        print(account)
    for transaction in customer.transactions:
        print(transaction)


def withdraw_money(self,customer):
    account_option = int(input("1.Checking 2.Savings"))
    if account_option == 1:
        for a in customer.accounts:
            if a.type == "Checking":
                account = a
    else:
        for a in customer.accounts:
            if a.type == "Savings":
                account = a
    money = float(input("Amount?"))
    print("Withdraw from account", account.type)
    logging.info("Withdraw %s from  %s", money, account.type)
    if account.available_balance < money:
        print("Available account balance " + str(account.available_balance)+"is less than ", str(money))
        return
    account.available_balance = account.available_balance - money
    account.current_balance = account.available_balance
    transaction = Transaction(account.id, "withdrawals", "withdrawal", "online banking", "Cash/Check withdrawal", datetime.now(), -money, datetime.now())
    customer.transactions.append(transaction)
    db_manager.create_customer(customer)
    logging.info("Withdraw successful")
    print("Withdraw successful")


def deposit_money(self,customer):
    account_option = int(input("1.Checking 2.Savings"))
    if account_option == 1:
        for a in customer.accounts:
            if a.type == "Checking":
                account = a
    else:
        for a in customer.accounts:
            if a.type == "Savings":
                account = a
    money = float(input("Amount?"))
    print("Deposit into account", account.type)
    logging.info("Deposit %s into  %s", money, account.type)
    account.available_balance = account.available_balance + money
    account.current_balance = account.available_balance
    transaction = Transaction(account.id, "Deposits", "Deposits", "online banking", "Cash/Check deposits", datetime.now(), money, datetime.now())
    customer.transactions.append(transaction)
    db_manager.create_customer(customer)


def create_account(type):
    logging.info("Creating %s account", type)
    if type == "Checking":

        return Checking(0, 0, 0, 0, round(100000*random.random()), round(100000*random.random()), 50, datetime.now())
    else:
        return Savings(0, 0, 0, 0, round(100000*random.random()), round(100000*random.random()), 2, 50, datetime.now())


if __name__ == "__main__":
    main()
