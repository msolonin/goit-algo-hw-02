# Завдання 1:
from queue import Queue
from typing import Any
import random
import time

QUEUE_LIMIT = 30
ID = 0
queue = Queue()


def generate_request(item: Any = None):
    """ Method for emulate generate request for add item
    :param item: any item, if none than generate random number
    :type item: Any
    """
    if not item:
        item = random.randrange(10 ** 3, 10 ** 5)
    global ID
    item = (ID, item)
    queue.put(item)
    print(f'Item: {item[1]} with id: {item[0]} was added')
    ID += 1


def process_request():
    """ Method for emulate process request
    """
    if queue.qsize() > 0:
        item = queue.get()
        print(f'Item: {item[1]} with id: {item[0]} was processed')
    else:
        print('No Items in Queue')


if __name__ == "__main__":
    for _ in range(QUEUE_LIMIT):
        random.choice([generate_request, process_request])()
        time.sleep(0.3)
