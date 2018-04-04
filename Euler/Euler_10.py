''' Euler 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
import numpy as np
# a painfully SLOW solution. 
# apparently the Sieve of Eratosthenes algorithm is best suited for this. This exercise highlights the need to know and understand existing algorithms so one doesn'y reinvent the wheel.

def prime_number(x):
    ''' Get all prime numbers that are less than x.
    '''
    n = 2

    while n < x:
        if np.all(n % np.arange(2,n)):
            yield n
        n += 1


# 142913828922
p = prime_number(2000000)
print(sum(p))
