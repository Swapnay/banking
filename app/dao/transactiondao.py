from app.banking.transaction import Transaction
from app.dao.dbinit import DBinit
import logging


class TransactionDao(object):
    logger = logging.getLogger('app.dao.TransactionDao')

    def __init__(self):
        pass

    def create_transaction(self, transaction_data):
        logging.info("create transaction %s", transaction_data.customer_id)
        with DBinit.db_session(self) as session:
            session.add(transaction_data)

    def get_transactions(self, customer_id):
        with DBinit.db_session(self) as session:
            transaction_data = session.query(Transaction).filter(Transaction.customer_id == customer_id ).first()
        return transaction_data
