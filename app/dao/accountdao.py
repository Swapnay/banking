from app.banking.account import Account
from app.dao.dbinit import DBinit
import logging


class AccountDao(object):
    logger = logging.getLogger('app.dao.AccountDao')

    def __init__(self):
        pass

    def create_update_account(self, customer, account_data):
        logging.info("create update account customer %s",customer.user_id)
        with DBinit.db_session(self) as session:
            session.add(customer)
            session.add(account_data)

    def get_account(self, id, type):
        logging.info("get Account %s", id)
        with DBinit.db_session(self) as session:
            employee_data = session.query(Account).filter(Account.id == id and Account.type == type).first()
        return employee_data

    def transfer_money(self, from_account, to_account, transaction_from, transaction_to, customer):
        logging.info("transfer money from account %s to account %s", from_account.type, to_account.type)
        with DBinit.db_session(self) as session:
            session.add(customer)
            session.add(from_account)
            session.add(to_account)
            session.add(transaction_from)
            session.add(transaction_to)
