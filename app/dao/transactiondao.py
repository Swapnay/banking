class TransactionDao(object):
    def create_transaction(self, tramsaction):
        try:
            session.add(tramsaction)
            session.commit()
        except Exception as ex:
            print(ex)
            session.rollback()
            raise ex