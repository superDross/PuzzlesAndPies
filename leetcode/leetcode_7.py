''' LeetCode 7

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''


def reverse(num):
    num_list = list(str(num))
    if num_list[0] == '-':
        reverse_num_list = ['-'] + num_list[1:][::-1]
    else:
        reverse_num_list = num_list[::-1]
    reversed_num = int(''.join(reverse_num_list))
    if abs(reversed_num) > 2147483647:
        return 0
    return reversed_num


print(reverse(-123999))
