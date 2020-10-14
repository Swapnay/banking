import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from app.banking.customer import Customer
from app.dao.dbinit import DBinit
import logging


class CustomerDao:
    logger = logging.getLogger('banking.bank.CustomerDao')

    def __init__(self):
        pass

    def create_customer(self, customer_data):
        logging.info("create customer %s", customer_data.user_id)
        with DBinit.db_session(self) as session:
            session.add(customer_data)

    def get_customer(self, user_id, password):
        logging.info("get customer %s", user_id)
        with DBinit.db_session(self) as session:
            custmer_data = session.query(Customer).filter(Customer.user_id == user_id
                                                          and Customer.password == password).first()
        return custmer_data

    def get_customer_by_id(self, id):
        logging.info("get customer by id %s", id)
        with DBinit.db_session(self) as session:
            custmer_data = session.query(Customer).filter(Customer.id == id).first()
        return custmer_data

    def delete_customer(self, customer_data):
        with DBinit.db_session(self) as session:
            session.delete(customer_data)
