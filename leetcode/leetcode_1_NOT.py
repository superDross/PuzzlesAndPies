''' LeetCode 1

Given an array of integers, return indices of the two numbers such that they
add up to a specific target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
import itertools


def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    combinations = itertools.combinations(enumerate(nums), 2)
    for x in combinations:
        if x[0][1] + x[1][1] == target:
            return (x[0][0], x[1][0])


nums = [2, 7, 11, 15]
target = 17
answer = two_sum(nums, target)
print(answer)
