from app.banking.employee import Employee
from app.dao.dbinit import DBinit
import logging


class EmployeeDao:
    logger = logging.getLogger('banking.bank.EmployeeDao')

    def __init__(self):
        pass

    def create_employee(self, employee_data):
        logging.info("create employee %s", employee_data.user_id)
        with DBinit.db_session(self) as session:
            session.add(employee_data)

    def get_employee(self, user_id, password):
        logging.info("get employee %s", user_id)
        with DBinit.db_session(self) as session:
            employee_data = session.query(Employee).filter(Employee.user_id == user_id
                                                           and Employee.password == password).first()
        return employee_data

    def delete_employee(self, employee_data):
        with DBinit.db_session(self) as session:
            session.delete(employee_data)
