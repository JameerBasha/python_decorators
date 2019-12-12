from functools import wraps
import time

def timer(func):
    
    def wrapper_function(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        end_time=time.time()
        return  end_time-start_time
    return wrapper_function


@timer
def add(x,y):
    return x+y

@timer
def add3(x,y,z):
    return x+y+z

@timer
def add_any(*args):
    return sum(args)

@timer
def abs_add_any(*args,**kwargs):
    total=sum(args)
    if kwargs.get('abs') is True:
        return abs(total)
    return total


print(add(1,2))
print(add3(1,2,3))
print(add_any(1,2,3,4))
print(abs_add_any(1,2,3,a=1,b=2,c=3))