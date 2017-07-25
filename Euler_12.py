import numpy as np


# add the natural sequence of all numbers to x; get the triangle number of x
tri_num = lambda x: np.sum(np.arange(1,x+1))

# vectorize allows one to apply a function to a list, sort of like numpys version of map
seq = np.vectorize(tri_num)

# triangle numbers upto x
tri_seq = seq(range(1, 100))

print(tri_seq)

# try this method: http://www.gmathacks.com/gmat-math/number-of-factors-of-a-large-integer.html
def find_factors(x):
    pass
