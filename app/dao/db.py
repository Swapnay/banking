import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from app.banking.customer import Customer
from app.banking.employee import Employee
from app.dao.dbinit import DBinit
import logging


class DbManager:
    logger = logging.getLogger('banking.bank.DbManager')

    def __init__(self):
        pass

    def create_employee(self, employee_data):
        with DBinit.db_session(self) as session:
            session.add(employee_data)

    def create_customer(self, customer_data):
        with DBinit.db_session(self) as session:
            session.add(customer_data)

    def get_employee(self, user_id, password):
        with DBinit.db_session(self) as session:
            employee_data = session.query(Employee).filter(Employee.user_id == user_id and Employee.password == password).first()
        return employee_data

    def get_customer(self, user_id, password):
        with DBinit.db_session(self) as session:
            custmer_data = session.query(Customer).filter(Customer.user_id == user_id and Customer.password == password).first()
        return custmer_data

    def delete_customer(self, customer_data):
        with DBinit.db_session(self) as session:
            session.delete(customer_data)
