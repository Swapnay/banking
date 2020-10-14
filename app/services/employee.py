from app.dao.employeedao import EmployeeDao
import logging


class EmployeeService:
    logger = logging.getLogger('app.services.EmployeeService')
    employeeDao = EmployeeDao()

    def __init__(self):
        pass

    def get_employee_details(self, emp_id, password):
        return self.employeeDao.get_employee(emp_id, password)
