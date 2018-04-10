''' LeetCode 8 - Atring to Integer (atoi)

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.


Requirements for atoi:

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
'''
import re


def atoi(s):
    s = s.lstrip()
    if not s or \
       s in ['-', '+'] or \
       (not s[0].isdigit() and
           s[0] not in ['+', '-']):
        return 0
    # identify unwnated characters in the string
    unwanted_chars = r'[ !"£$%^&*(){};:\'\\\@#~<>,./?|`¬_=a-zA-Z]'
    matches = re.compile(unwanted_chars).finditer(s)
    # Get the first match index and slice upto that point
    if list(matches):
        l = sorted([m.start() for m in re.compile(unwanted_chars).finditer(s)])
        i = l[0]
        s = s[:i]
    try:
        conversion = int(s)
    except ValueError:
        return 0
    # Deal with Max and Min integers
    if conversion < -2147483648:
        return -2147483648
    elif conversion > 2147483647:
        return 2147483647
    return conversion


assert atoi('-0908o999') == -908
assert atoi('abc') == 0
assert atoi('  +0 123') == 0
assert atoi('-2147483648') == -2147483648
assert atoi('23a8f') == 23
assert atoi('123  456') == 123
