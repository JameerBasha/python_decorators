from functools import lru_cache

@lru_cache(maxsize=100000)
def factorial(n):
    print("Computing factorial({})".format(n))
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(factorial(100))