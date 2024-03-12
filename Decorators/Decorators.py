# creating a decorator
# creating a function that needs to be passed into the decorator
# testing the decorator

import time


def functionspeed(func):
    def wrapper():
        a = time.time()
        func()
        b = time.time()
        print(b - a)
        return 0
    return wrapper


@functionspeed
def my_function():
    for i in range(2000):
        b: int = int(i / 3)
        for c in range(b):
            time.sleep(0.01)
            return c


my_function()
