from app.dao.customerdao import CustomerDao
from app.banking.customer import Customer
from datetime import datetime
import logging


class CustomerService:
    logger = logging.getLogger('app.services.CustomerService')
    customer_dao = CustomerDao()

    def __init__(self):
        pass

    def get_customer_details(self, user_id, password):
        return self.customer_dao.get_customer(user_id, password)

    def save_customer_details(self, first_name, last_name, email, home_phone, cell_phone, address, user_id, password, employee_id):
        try:
            customer = Customer(first_name, last_name, email, home_phone, cell_phone, address, user_id, password, datetime.now(), datetime.now(), employee_id)
            self.customer_dao.create_customer(customer)
            return self.customer_dao.get_customer(user_id, password)
        except Exception as ex:
            logging.error("Save customer details %s", ex)
