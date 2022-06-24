from src import utils

print(dir(utils))

from src.utils.logger import get_logger

log = get_logger()

try:
    print(hello)
except Exception as e:
    for _ in range(100000):
        log.error(e)
    print('exception logged')