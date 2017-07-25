''' Euler 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
import numpy as np

# slow answer

def prime_number(x):
    ''' Get the x sequential prime number.
        e.g. if x=100, get the 100th prime 
        number
    '''
    store = []
    n = 2

    while len(store) < x:
        if np.all(n % np.arange(2,n)):
            store.append(n)
        n += 1

    return store[-1]

# 104743
answer = prime_number(10001)
print(answer)
