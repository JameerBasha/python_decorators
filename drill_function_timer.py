import math
import time

def timer(func):
    def getTime(x):
        start_time=time.time()
        time.sleep(1)
        func(x)
        end_time=time.time()
        return end_time-start_time
    return getTime
@timer
def sqrt(x):
    return math.sqrt(x)

@timer
def square(x):
    return x*x

print(sqrt(10))
print(square(10))