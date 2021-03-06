''' Euler 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
import numpy as np

# Slow answer. I am sure there is an algorithm out there to speed thid function up.

def prime_number(x):
    ''' Get the x sequential prime number.
        e.g. if x=100, get the 100th prime 
        number
    '''
    n = 2
    c = 0 # counts number of prime numbers iterated through

    while c < x:
        if np.all(n % np.arange(2,n)):
            c += 1
            yield n
        n += 1


# 104743
answer = prime_number(10001)
print(list(answer)[-1])
