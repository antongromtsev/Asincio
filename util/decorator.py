import time
import datetime


def timer(func):
    def _wrapper(*args, **kwargs):
        t1 = time.perf_counter()
        func(*args, **kwargs)
        t2 = time.perf_counter()
        print('Время выполнения:', t2 - t1, 'сек')
    return _wrapper


def log(func):
    i = 0

    def _wrapper(*args, **kwargs):
        nonlocal i
        i += 1
        with open('debug.log', 'at') as f:
            f.writelines(f'{func.__name__} {i} {datetime.datetime.now()} \n')
        return func(*args, **kwargs)
    return _wrapper
