''' Euler 20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''
import numpy as np
# object dtype required for returning large numbers
r = np.arange(1, 101, dtype='object')
n = np.multiply.reduce(r)
z = [int(x) for x in str(n)]
answer = np.sum(z)
# 648
print(answer)
