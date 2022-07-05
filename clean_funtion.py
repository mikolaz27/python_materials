import random
from functools import lru_cache


# def unclean_function():
#     print("Side effect of unclean_function")
#     return random.randint(0, 1000)
#
#
# print(unclean_function())
#
#
# def clean_function(a):
#     print("Side effect of clean_function")
#     return a * a
#
#
# print(clean_function(5))


# @lru_cache(4)
# def unclean_cached_function():
#     result = random.randint(0, 1000)
#     return f"result is {result}"
#
#
# for _ in range(5):
#     print(unclean_cached_function())


@lru_cache(4)
def clean_cached_function(a):
    result = random.randint(a, 1000)
    return f"result is {result}"


for i in range(5):
    print(clean_cached_function(i))


