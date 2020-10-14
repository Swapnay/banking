from sqlalchemy import Column, String, Integer, DateTime
from app.dao.dbinit import DBinit


class Employee(DBinit.Base):
    __tablename__ = 'employee'
    id = Column('id', Integer(), primary_key=True)
    first_name = Column('first_name', String(255), nullable=False)
    last_name = Column('last_name', String(255), nullable=False)
    email = Column('email', String(255), nullable=False, unique=True)
    home_phone = Column('home_phone', String(255))
    cell_phone = Column('cell_phone', String(255))
    address = Column('address', String(255), nullable=False)
    user_id = Column('user_id', String(255), nullable=False, unique=True)
    password = Column('password', String(255), nullable=False)
    created_time = Column('created_time', DateTime)
    updated_time = Column('updated_time', DateTime)

    def __init__(self, first_name, last_name, email, home_phone, cell_phone, address, user_id, password, created_time, updated_time, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.home_phone = home_phone
        self.cell_phone = cell_phone
        self.address = address
        self.user_id = user_id
        self.password = password
        self.created_time = created_time
        self.updated_time = updated_time
        self.id = id

    def __str__(self):
        return "Employee: Name  % s % s, \n" \
               "UserId % s, Cell Phone % s \n " \
               "Email % s, Home Phone % s \n" \
               "Address % s" % (self.first_name, self.last_name, self.user_id, self.cell_phone, self.email, self.home_phone, self.address)
