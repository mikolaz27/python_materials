import time
import threading
import multiprocessing
import multiprocess
import itertools
import os
import logging
import random
import string
import requests
from functools import partial

class timer():
    def __init__(self, message):
        self.message = message

    def __enter__(self):
        self.start = time.time()
        return None

    def __exit__(self, type, value, traceback):
        elapsed_time = (time.time() - self.start)
        print(self.message.format(elapsed_time))

def factorize_naive(n):
    """ A naive factorization method. Take integer 'n', return list of
        factors.
    """
    if n < 2:
        return []
    factors = []
    p = 2

    while True:
        if n == 1:
            return factors

        r = n % p
        if r == 0:
            factors.append(p)
            n = n / p
        elif p * p >= n:
            factors.append(n)
            return factors
        elif p > 2:
            # Advance in steps of 2 over odd numbers
            p += 2
        else:
            # If p == 2, get to 3
            p += 1

    assert False, "unreachable"

DATA_SIZE = 1_000
result = {}
workers = 16
with timer('Elapsed: {}s'):
    with multiprocessing.Pool(workers) as pool:
        input_data = (i for i in range(1, DATA_SIZE + 1))
        result = [
            (n, factors)
            for n, factors in
            enumerate(pool.map(factorize_naive, input_data), 1)
        ]

print(len(result), result[:100])

result = {}
workers = 16
with timer('Elapsed: {}s'):
    with ThreadPool(workers) as pool:
        input_data = (i for i in range(1, DATA_SIZE + 1))
        result = [
            (n, factors)
            for n, factors in
            enumerate(pool.map(factorize_naive, input_data), 1)
        ]

print(len(result), result[:100])