import os
import psutil
import ra as ra


def memory_usage(func):
    def internal(*args, **kwargs):
        process = psutil.Process(os.getpid())
        memory_before = process.memory_info().rss
        result = func(*args, **kwargs)
        memory_after = process.memory_info().rss
        print(
            f'Usage of memory by function {func.__name__}: {memory_after - memory_before}')
        return result

    return internal


@memory_usage
def _test():
    sum = 0
    for i in range(1_000_000_000):
        sum += i
    return sum

_test()