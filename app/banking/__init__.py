import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
import logging.config
from app.util import PathUtil

log_conf = PathUtil.get_empyreal_path().joinpath('app/logging.conf')
log_path = PathUtil.get_empyreal_path().joinpath('logs').joinpath('banking.log')
log_path.parent.mkdir(parents=True, exist_ok=True)

logging.config.fileConfig(fname=log_conf,
                          defaults={'logfilename': log_path},
                          disable_existing_loggers= True)