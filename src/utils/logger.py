import logging
import sys
from logging.handlers import TimedRotatingFileHandler
from logging.handlers import RotatingFileHandler
FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
LOG_FILE = "info.log"

def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler

def get_file_handler():
    # This will create a new log file every midnight, and 5 backup files with a timestamp before overwriting old logs.
    file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight', backupCount=5)
    # roll over after 2KB, and keep backup logs app.log.1, app.log.2 , etc.
    # file_handler = RotatingFileHandler(LOG_FILE, maxBytes=2000, backupCount=5)
    file_handler.setFormatter(FORMATTER)
    return file_handler

def get_logger():
    """
    import function and set log = get_logger()
    log.info('message')
    log.error('message'), add 'exc_info=True' for teace back
    log.exception('message'), traceaback is also included
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG) # better to have too much log than not enough
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    # with this pattern, it's rarely necessary to propagate the error up to parent
    logger.propagate = False
    return logger