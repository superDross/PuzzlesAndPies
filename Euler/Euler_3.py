''' Euler 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
import numpy as np

# works but not with low numbers such as 24, as the 'n' number is not divided. The try/except is the bottleneck here and I suspect the solution is needlessly complex. Perhaps a While loop approach would be best.

def largest_prime_factor(n, num=100):
    try:
        r = np.arange(2, num)
        f = r[n % r == 0] # this is incorrect, re-read about prime numbers
        prime_factors = (f[:i] for i in range(2, len(f)) if np.multiply.reduce(f[:i]) == n)
        array = next(prime_factors)
        return array[-1]
    
    except StopIteration:
        return largest_prime_factor(n, num*10)


n = 600851475143

# 6857
largest_prime_factor(n)
