import time
from statistics import mean, stdev

class Timer:
    def __init__(self):
        self.restart()

    def start(self):
        self.restart()

    def end(self):
        self.time = time.time() - self.start

    def restart(self):
        self.start = time.time()
        self.time = None

    def report(self):
        print(f"Timer ran in {self.time:.6f}s")


def timer(print_=False):
    def inner2(func):
        def inner(*args, **kwargs):
            st = time.time()
            ret = func(*args, **kwargs)
            if print_:
                print(f"{func.__name__} ran in {time.time()-st:.2f}s")
                return ret
            else:
                delta = time.time() - st
                return ret, delta
        return inner
    return inner2


class TimeStatisticsCalculator:
    def __init__(self):
        self.times = []

    def __call__(self, function, *args, **kwargs):
        self.functionName = function.__name__
        ret, delta = timer()(function)(*args, **kwargs)
        self.times.append(delta)

    def report(self):
        self.times = list(map(lambda v: 1e6*v, self.times))
        mean, stdValue = self.computeStatistics()
        print(f"Executed the function {len(self.times)} times with a mean execution time of {mean:.2f} +- {stdValue:.2f}us")

    def computeStatistics(self):
        return mean(self.times), stdev(self.times)
