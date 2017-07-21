''' Euler 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
import numpy as np


def test(p, x=0, l=[]):
    x = p/2
    n = 2
    
    while True:
        if np.multiply.reduce(l) == p:
            print(l)
            break

        if x % n == 0:
            l.append(n)
            return 

