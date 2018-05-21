''' LeetCode 17 - Letter Combonations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
'''
d = {'1': '',
     '2': ['a', 'b', 'c'],
     '3': ['d', 'e', 'f'],
     '4': ['g', 'h', 'i'],
     '5': ['j', 'k', 'l'],
     '6': ['m', 'n', 'o'],
     '7': ['p', 'q', 'r', 's'],
     '8': ['t', 'u', 'v'],
     '9': ['w', 'x', 'y', 'z']}


def solution(digits, l=[], index=1):
    if len(digits) == 1:
        return d.get(digits)
    if digits == '':
        return ''
    all_digits = [d.get(digit) for digit in list(digits)]
    l = all_digits[0] if not l else l
    new = []
    for chars in l:
        for char in all_digits[index]:
            new.append(''.join((chars, char)))
    if index >= len(all_digits) - 1:
        return new
    return solution(digits, new, index=index + 1)


assert solution('234') == ['adg', 'adh', 'adi', 'aeg', 'aeh', 'aei', 'afg', 'afh', 'afi', 'bdg', 'bdh', 'bdi',
                           'beg', 'beh', 'bei', 'bfg', 'bfh', 'bfi', 'cdg', 'cdh', 'cdi', 'ceg', 'ceh', 'cei', 'cfg', 'cfh', 'cfi']
assert solution('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
