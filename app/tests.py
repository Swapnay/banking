from app.dao.db import CustomerDao
from .banking.customerprofile import Customer, Checking, Savings
import unittest
from datetime import datetime
from parameterized import parameterized
import logging


class TestSuite(unittest.TestCase):
    logger = logging.getLogger('models.global_config')
    customer1 = Customer("test_name", "test_last", "test@test.com", "333-444-5678", "444-555-6789", "1234 Lake Lane , Sunnyvale CA", "testuser", "Mi4man11", datetime.now(), datetime.now())
    savings = Savings(2300, 0, 0, 2300, 12345, 23456, 2, 50, datetime.now())
    checking = Checking(400, 0, 0, 300, 34567, 56789, 30, datetime.now())

    @parameterized.expand([
        (customer1, savings, checking, True),
        (customer1, savings, checking, True)
    ])
    def test_create_customer(self, customer_data, savings_data, checking_data, expected):
        try:

            CustomerDao.create_customer(self, customer_data)
            customer_details = CustomerDao.get_user(self, customer_data.user_id, customer_data.password)
            self.assertTrue(customer_data.user_id == customer_details.user_id)
            customer_details.accounts.append(savings_data)
            customer_details.accounts.append(checking_data)
            CustomerDao.create_customer(self, customer_details)
            customer_account_details = CustomerDao.get_user(self, customer_data.user_id, customer_data.password)
            self.assertTrue(len(customer_account_details.accounts) == 2)

        except Exception as e:
            logging.error(e)
            self.assertFalse(expected)

    @classmethod
    def tearDownClass(cls):
        try:
            CustomerDao.delete_customer(cls, cls.customer1)
        except Exception as ex:
            print(ex)
            logging.error("unable to delete rows ", ex)



if __name__ == '__main__':
    unittest.main()
