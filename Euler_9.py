''' Euler 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def py_triplet(x):
    ''' Get the pythagorean triplet
        when only given the summary
        of the triplet.
    '''
    sqrt = lambda x: x**(1/2)

    for a in range(1, x):
        for b in range(1, x):
            c = sqrt((a**2) + (b**2))
            abc = a+b+c
            
            if abc == x and a < b < c:
                return a, b, c
               
            elif c > x:
                b = 0
                break


# (200, 375, 425) 
answer = py_triplet(1000)
print(answer)
