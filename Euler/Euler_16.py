''' Euler 16

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
'''
import numpy as np

# 1366
n = [int(x) for x in str(2**1000)]
answer = np.sum(n)
