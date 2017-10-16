''' Euler 21

let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
def proper_divisors(n):
    for x in range(1, n):
        if (n/x) % 2 in [1, 0]:
            yield x

def amicable_number(a, last=0):
    b = sum(proper_divisors(a))
    c = sum(proper_divisors(b))
    if a == c and a != b:
        return a

def sum_of_amicable_pairs(n): 
    arr = (amicable_number(x) for x in range(1, n))
    clean_arr = (x for x in arr if x)
    return sum(clean_arr)

if __name__ == "__main__":
    # 31626 
    answer = sum_of_amicable_pairs(10000)
    print(answer)
