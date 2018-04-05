''' LeetCode 9

Determine whether an integer is a palindrome. Do this without extra space.
'''


def is_palindrome(x):
    if x < 0:
        return False
    x_list = list(str(x))
    x_reverse = int(''.join(x_list[::-1]))
    if x == x_reverse:
        return True
    else:
        return False


print(is_palindrome(-9009))
