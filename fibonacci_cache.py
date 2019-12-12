memoize_table={}

def memoize(original_function):
    
    def wrapper_function(n):
        if(n in memoize_table):
            return memoize_table[n]
        else:
            memoize_table[n]=original_function(n)
            return memoize_table[n]
    return wrapper_function

@memoize
def fib(n):
    print("Computing fib({})".format(n))
    if n in [0, 1]:
        return n
    return fib(n - 1) + fib(n - 2)

fib(10)