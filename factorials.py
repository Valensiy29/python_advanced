import logging
import math
import time
from multiprocessing import Pool

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

start_time = time.time()

def task(num):
    return math.factorial(num)

end_time = time.time()
logger.info(f'{end_time-start_time}')

def apply_async():
    start_time = time.time()
    with Pool() as pool:
        result = pool.apply_async(task)
    end_time = time.time()
    logger.info(f'{end_time-start_time}')




if __name__ == '__main__':
    apply_async()
    num = 10000