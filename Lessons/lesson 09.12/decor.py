import time
import logging

logging.basicConfig(filename='log.log', encoding='utf-8', level=logging.DEBUG)

logging.error("test error")
logging.warning("test warning")

def log(f):
    def wrapper(*args, **kwargs):
        logging.debug(f"function name: {f.__name__}")
        logging.debug(f"function args: {', '.join(map(str, args))}")
        logging.debug(f"function name: {kwargs.items()}")
        start = time.time()
        res = f(*args, **kwargs)
        finish = time.time()
        logging.debug(f"function time: {finish - start}")
        logging.debug(f"function result: {res}")
        return res
    return wrapper

@log
def sum(x, y):
    return x+y

print(sum(2, 3))

@log
def load(x):
    for i in range(x):
        i*i

load(100000)