''' Euler 6

The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
import numpy as np

# the sum of the square
sm = np.sum(np.arange(1,101) ** 2)

# square of the sum of the first ten nums
sq = np.sum(np.arange(1,101)) ** 2

# 25164150
diff = sq-sm
print(diff)
