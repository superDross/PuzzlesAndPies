''' Euler 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''
import numpy as np

def largest_palindrome(n):
    r = np.arange(1, n)[::-1]
    # reversing the number by changing type is likely the bottle neck
    g = ((x*y, x,y) for x in r for y in r if x*y == int(str(x*y)[::-1]))
    arr = np.array(list(g))
    p = np.argsort(arr[:, 0])[-1]
    return arr[p]

# 906609 = 993 * 913
answer = largest_palindrome(1000)
print(answer)
