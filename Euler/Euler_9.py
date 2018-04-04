''' Euler 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
import numpy as np

def py_triplet(x):
    ''' Get the pythagorean triplet when only 
        given the summary of the triplet.
    '''
    a = np.arange(1, x)
    b = np.arange(1, x)
    c = np.sqrt((a[:, np.newaxis] ** 2) + (b ** 2))
    # get all additional combinations of a, b & c
    ab = a[:, np.newaxis] + b
    abc = c+ab
    # find indexes containing value x, no need to check more than one
    coords = np.where(abc == x)
    x, y = list(coords[0])
    return a[x], b[y], c[x, y]


# (200, 375, 425)
answer = py_triplet(1000)
print(answer)
