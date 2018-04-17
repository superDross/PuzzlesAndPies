''' Euler 1

If we list all the natural numbers below 10 that are multiples
of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
import numpy as np
import time


def sum_of_multiples_np():
    arr = np.arange(1000)
    n = arr[(arr % 3 == 0) | (arr % 5 == 0)]
    total = np.sum(n)
    return total


def sum_of_multiples():
    ''' Using a list to store all multiples.'''
    all_multiples = [n for n in range(1, 1000) if n % 3 == 0 or n % 5 == 0]
    return sum(all_multiples)


def sum_of_multiples_gen():
    ''' Using a generator expression.'''
    for n in range(1, 1000):
        if n % 3 == 0 or n % 5 == 0:
            yield n


# Answer = 233168
# Standard Python
t0 = time.time()
answer = sum_of_multiples()
t1 = time.time()

# Generator Expression
answer_gen = sum(sum_of_multiples_gen())
t2 = time.time()

# NumPy
answer_np = sum_of_multiples_np()
t3 = time.time()


print('sum_of_multiples()', answer, '\n',
      '{:.3e}'.format(t1 - t0), 'Seconds\n')
print('sum_of_multiples_gen()', answer_gen, '\n',
      '{:.3e}'.format(t2 - t1), 'Seconds\n')
print('sum_of_multiples_np()', answer_np, '\n',
      '{:.3e}'.format(t3 - t2), 'Seconds\n')
