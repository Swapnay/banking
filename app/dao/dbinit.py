import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
import sqlalchemy as db
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.dbconfig import connection_str
from contextlib import contextmanager


class DBinit(object):
    engine = db.create_engine(connection_str, echo=True)
    Base = declarative_base(bind=engine)
    Session = sessionmaker(autocommit=False, autoflush=True, expire_on_commit=False, bind=engine)

    @contextmanager
    def db_session(self):
        session = scoped_session(DBinit.Session)
        try:
            yield session
            session.commit()
        except Exception as ex:
            print("Error during databse connection{}", ex)
            session.rollback()
            raise
        finally:
            session.expunge_all()
            session.close()

