from email import message
import logging
import sys
import os
from logging.handlers import TimedRotatingFileHandler


FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
LOG_FILE = "events.log"
DEFAULT_LOG_ID = "DEBUG-1"

def get_console_handler():
   console_handler = logging.StreamHandler(sys.stdout)
   console_handler.setFormatter(FORMATTER)
   return console_handler

def get_file_handler():
   file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
   file_handler.setFormatter(FORMATTER)
   return file_handler

def get_logger(logger_name):
   logger = logging.getLogger(logger_name)
   logger.setLevel(logging.DEBUG) # better to have too much log than not enough
   logger.addHandler(get_console_handler())
   logger.addHandler(get_file_handler())
   # with this pattern, it's rarely necessary to propagate the error up to parent
   logger.propagate = False
   return logger

def set_logger(propagate=False, dir_path=None, filename=None):
    if dir_path is None:
        dir_path = os.path.dirname(os.path.realpath(__file__))
    if filename is None:
        filename='events.log'
    file_handler = logging.FileHandler(os.path.join(dir_path, filename))
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(FORMATTER)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    logger.propagate = propagate
    return logger

def log(message, exception=None, propagate=False, dir_path=None, filename=None, log_level='info'):
    logger = set_logger(propagate=propagate)
    logger.info(message)

class EscapeLogger():

    def __init__(self, filename: str = 'events.log', context: dict = {}) -> None:
        self.context = context
        self.log_filename = filename

if __name__=='__main__':
    log(message='killer', log_level='info')
    logger = set_logger
    logger.debug('lkdl')