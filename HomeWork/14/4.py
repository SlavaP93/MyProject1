import time

def timer(func):
    def timer_func(*args):
        start = time.time()
        n = func(*args)
        finish = time.time()
        times = finish - start
        print(times)
        return n
    return timer_func
@timer
def power(a, n):
    if n == 1:
        return n
    return a * power(a, n - 1)

print(power(2,3))
