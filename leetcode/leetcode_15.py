''' LeetCode 15 - 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
import itertools


def solution(nums):
    l = []
    combos = itertools.combinations(nums, 3)
    for combo in combos:
        combo = sorted(combo)
        if sum(combo) == 0 and combo not in l:
            l.append(combo)

    return sorted(l)


assert solution([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
