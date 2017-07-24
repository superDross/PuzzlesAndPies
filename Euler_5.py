''' Euler 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
import numpy as np
import itertools


# Since we knwo 2520 is evenly divisible by the 1-10
# then the number we want is an increment of 2520

def main():
    n = 2520
    r = np.arange(1,21)
    z = np.any(n % r > 0)

    while z:
        n += 2520
        z = np.any(n % r > 0)

    return n

# 232792560
answer = main()
print(answer)
