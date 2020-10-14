import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
import logging
from sqlalchemy_utils import database_exists, create_database
from app.services.employee import EmployeeService
from app.services.customer import CustomerService
from app.services.account import AccountService, CheckingService, SavingsService, LoanService, CreditService
from app.dao.dbinit import DBinit


class BankingManager(object):
    logger = logging.getLogger('banking.bank.BankingManager')

    def __init__(self):
        pass

    def create_data_base(self):
        if not database_exists(DBinit.engine.url):
            create_database(DBinit.engine.url)
        DBinit.Base.metadata.create_all(DBinit.engine)

    employee_service = EmployeeService()
    customer_service = CustomerService()
    account_service = AccountService()

    '''Employee Login Flow - Create customer and Create accounts'''
    '''Customer Login Flow - transfer, withdraw and deposit money'''

    def main(self):
        try:
            self.create_data_base()
            print("Enter a choice ")
            choice = int(input("1.Employee Login 2. Customer Login 1/2?"))
            logging.info("Entered Choice %s", choice)
            if choice == 1:
                employee = self.employee_login()
                if employee is None:
                    return
                choice = input("Create Customer Y/N?")
                if choice.lower() == 'y':
                    customer = self.create_customer(employee.id)
                    self.create_account(customer, employee.id)
                    print("Customer created successfully. Exiting the application")
                return
            else:
                customer = self.customer_login()
                if customer is None:
                    return
            logging.info("Customer Details %s", customer)
            self.customer_actions(customer)
        except Exception as ex:
            logging.error("Error customer actions %s", ex)


    ''' Customer actions like Transfer,Check profile,Withdraw Money,Deposit,Logout'''

    def customer_actions(self, customer):
        try:
            while True:
                print("Select from below")
                print("1.Transfer 2.Check profile 3.Withdraw Money 4.Deposit 5.Logout")
                choice = int(input("Enter a choice between 1-5"))
                if choice == 1:
                    logging.info("Transfer Money")
                    customer = self.transfer_money(customer)
                elif choice == 2:
                    logging.info("Display Profile")
                    try:
                        self.print_customer_details(customer)
                    except Exception as e:
                        logging.error("Error while displaying profile details %s", e)
                        print("Error while displaying profile details ", e)
                        break
                elif choice == 3:
                    try:
                        self.withdraw_money(customer)
                    except Exception as e:
                        logging.error("Error while withdraw money %s", e)
                        print("Error while withdraw money ", e)
                        break
                elif choice == 4:
                    try:
                        self.deposit_money(customer)
                    except Exception as e:
                        logging.error("Error while deposit money %s", e)
                        print("Error while deposit money ", e)
                        break
                else:
                    logging.info("Log out")
                    print("Logging out..")
                    break
        except Exception as ex:
            logging.error("Error customer actions %s", ex)

    '''Transfer money from Checking/Savings to checking/savings/loan accounts'''
    def transfer_money(self, customer):
        try:
            print("select an account to transfer money from")
            from_acc = int(input("1.Checking 2.Savings 1/2"))
            print("select an account to transfer money to")
            to_acc = int(input("1.Checking 2.Savings 3.Loan 1-3"))
            while from_acc == to_acc:
                to_acc = int(input("1.Checking 2.Savings 3.Loan 1-3"))
            amount = float(input("Enter Amount"))
            if from_acc == 1:
                from_account = self.get_account_by_type(customer, "Checking")
            else:
                from_account = self.get_account_by_type(customer, "Savings")

            if to_acc == 1:
                to_account = self.get_account_by_type(customer, "Checking")
            elif to_acc == 2:
                to_account = self.get_account_by_type(customer, "Savings")
            else:
                to_account = self.get_account_by_type(customer, "Loan")
                return LoanService().transfer_money(from_account, to_account, amount, customer)

            return self.account_service.transfer_money(from_account, to_account, amount, customer)
        except Exception as ex:
            logging.error("Error transfer money %s", ex)

    def employee_login(self):
        user_id = input("Enter UserID")
        password = input("Enter Password")
        try:
            employee = self.employee_service.get_employee_details(user_id, password)
            return employee
            if employee is None:
                print("Incorrect user id or password ", user_id)
                return
        except Exception as ex:
            print("Incorrect user id or password ", ex)
            logging.error("Incorrect user id or password for user %s %s", user_id, ex)
            return

    def customer_login(self):
        user_id = input("Enter UserID")
        password = input("Enter Password")
        try:
            customer = self.customer_service.get_customer_details(user_id, password)
            return customer
            if customer is None:
                print("Incorrect user id or password ", user_id)
                return
        except Exception as ex:
            print("Incorrect user id or password ", user_id)
            logging.error("Incorrect user id or password for user %s", user_id)
            return

    def create_customer(self, employee_id):
        try:
            first_name =''
            last_name = ''
            password = ''
            userid = ''
            print("Creating Customer")
            while not first_name.strip():
                first_name = input("Enter First Name")
            while not last_name.strip():
                last_name = input("Enter Last Name")
            email = input("Email")
            home_phone = input("Home Phone")
            cell_phone = input("Cell Phone")
            address = input("Address")
            while not userid.strip():
                userid = input("UserId")
            while not password.strip():
                password = input("Password")
            customer = self.customer_service.save_customer_details(first_name, last_name, email, home_phone, cell_phone, address, userid, password, employee_id)
            return customer
        except Exception as ex:
            logging.error("Create customer %s", ex)

    '''Employee to create customer checking,savings, loan and credit card accounts'''
    def create_account(self, customer, emp_id):
        accounts = []
        while True:
            try:
                print("Create an account.")
                choice = int(input("1.Checking 2.Savings 3.Loan service 4. Credit card. 5.Exit enter a number between 1-5 to create an account? "))
                if choice == 1:
                    initial_amount = self.enter_amount()
                    account = CheckingService().create_account_details(initial_amount, 0, 0, 0, emp_id, customer)
                elif choice == 2:
                    initial_amount = self.enter_amount()
                    account = SavingsService().create_account_details(initial_amount, 0, 0, 0, emp_id, customer)
                elif choice == 3:
                    initial_amount = self.enter_principal()
                    interest = self.enter_interest_rate()
                    term = self.enter_term()
                    account = LoanService().create_account_details(0, initial_amount, interest, term, emp_id, customer)
                elif choice == 4:
                    account = CreditService().create_account_details(0, 0, 0, 0, emp_id, customer)
                else:
                    return accounts
                # return account
                accounts.append(account)
            except Exception as ex:
                logging.error("Error while create account %s ", ex)
        return accounts

    def print_customer_details(self, customer):
        print("Customer Details:")
        print(customer)
        for account in customer.accounts:
            print(account)
        for transaction in customer.transactions:
            print(transaction)

    def get_account_by_type(self, customer, type):
        for a in customer.accounts:
            if a.type == type:
                return a

    def withdraw_money(self, customer):
        account_option = int(input("1.Checking 2.Savings"))
        if account_option == 1:
            account = self.get_account_by_type(customer, "Checking")
        else:
            account = self.get_account_by_type(customer, "Savings")
        money = float(input("Amount?"))
        print("Withdraw from account", account.type)
        logging.info("Withdraw %s from  %s", money, account.type)
        self.account_service.withdraw_money(account, money, customer)
        logging.info("Withdraw successful")
        print("Withdraw successful")

    def deposit_money(self, customer):
        account_option = int(input("1.Checking 2.Savings 3.Loan 4. CreditCard"))
        if account_option == 1:
            account = self.get_account_by_type(customer, "Checking")
        else:
            account = self.get_account_by_type(customer, "Savings")
        money = float(input("Amount?"))
        print("Deposit into account", account.type)
        logging.info("Deposit %s into  %s", money, account.type)
        self.account_service.deposit_money(account, money, customer)

    def enter_amount(self):
        while True:
            try:
                amount = float(input("Please enter amount? "))
            except ValueError:
                print("Sorry, I didn't understand that.")

                continue
            else:
                return amount
                break

    def enter_principal(self):
        while True:
            try:
                amount = float(input("Please enter principal? "))
            except ValueError:
                print("Sorry, I didn't understand that.")

                continue
            else:
                return amount
                break

    def enter_interest_rate(self):
        while True:
            try:
                interest = float(input("Please enter interest rate? "))
            except ValueError:
                print("Sorry, I didn't understand that.")

                continue
            else:
                return interest
                break

    def enter_term(self):
        while True:
            try:
                term = int(input("Please term? "))
            except ValueError:
                print("Sorry, I didn't understand that.")

                continue
            else:
                return term
                break


if __name__ == "__main__":
    banking_manager = BankingManager()
    banking_manager.main()
