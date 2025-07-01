import timeit
import numpy
#%%
"""
Sum the numbers from 0 to n-1 in different ways.
"""
#%%
def for_loop(n=100_000_000):
    s = 0
    for i in range(n):
        s += i
    return s

print(f"pure for:\t{timeit.timeit(for_loop, number=1)}")
#%%
def while_loop(n=100_000_000):
    s = 0
    i = 0
    while i < n:
        s += i
        i += 1
    return s

print(f"while loop:\t{timeit.timeit(while_loop, number=1)}")
#%%
def for_loop_with_increment(n=100_000_000):
    s = 0
    for i in range(n):
        s += i
        i += 1
    return s

print(f"for loop with increment:\t{timeit.timeit(for_loop_with_increment, number=1)}")
#%%
def for_loop_with_if(n=100_000_000):
    s = 0
    for i in range(n):
        s += i
        if i < n:pass
    return s

print(f"for_loop_with_if:\t{timeit.timeit(for_loop_with_if, number=1)}")
#%%
def for_loop_with_if_and_increment(n=100_000_000):
    s = 0
    for i in range(n):
        s += i
        if i < n:pass
        i += 1
    return s

print(f"for_loop_with_if_and_increment:\t{timeit.timeit(for_loop_with_if_and_increment, number=1)}")
#%%
def sum_range(n=100_000_000):
    return sum(range(n))

print(f"sum_range:\t{timeit.timeit(sum_range, number=1)}")
#%%
def sum_generator(n=100_000_000):
    return sum(i for i in range(n))

print(f"sum_generator:\t{timeit.timeit(sum_generator, number=1)}")
#%%
def sum_list_comp(n=100_000_000):
    return sum([i for i in range(n)])

print(f"sum_list_comp:\t{timeit.timeit(sum_list_comp, number=1)}")
#%%
def sum_numpy(n=100_000_000):
    return numpy.sum(numpy.arange(n, dtype=numpy.int64))

print(f"sum_numpy:\t{timeit.timeit(sum_numpy, number=1)}")
#%%
def sum_numpy_python_range(n=100_000_000):
    return numpy.sum(range(n))

print(f"sum_numpy_python_range:\t{timeit.timeit(sum_numpy_python_range, number=1)}")
#%%
def sum_math(n=100_000_000):
    return (n * (n-1))//2

print(f"sum_math:\t{timeit.timeit(sum_math, number=1)}")