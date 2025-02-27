from time import sleep
import random
from datetime import datetime
import itertools as it
import types

def producer():
    'produce timestamps'
    starttime = datetime.now()
    while True:
        sleep(random.uniform(0,0.2))
        yield datetime.now()-starttime

def tracker(p,limit=2):
    """
    Generators that tracks the output of the producer and returns
    the number of odd numbered seconds that have been iterated over.

    :param p: The producer generator that returns the duration of its lifetime when called.
    :param limit: The number of odd-numbered seconds to track until completion.

    :return: The number of odd numbered seconds that have been iterated over.
    """
    assert(isinstance(p, types.GeneratorType)), "p must be a generator"
    assert(isinstance(limit, int) and limit > 0), "limit must be an int greater than 0"
    count = 0
    while count < limit:
        time = next(p)
        time = int(time.total_seconds())
        if time % 2 == 1:
            count += 1
        new_limit = yield count
        if new_limit is not None:
            limit = new_limit
