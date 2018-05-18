''' LeetCode 16 - 3Sum Closest

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

import itertools


def solution(nums, target):
    best = tuple()
    combos = itertools.combinations(nums, 3)
    for combo in combos:
        combo = sorted(combo)
        total = sum(combo)
        difference = abs(total - target)
        diff_tuple = (combo, difference, total)

        if not best:
            best = diff_tuple
        elif best[1] > diff_tuple[1]:
            best = diff_tuple

    return best[2]


assert solution([-1, 2, 1, -4], 1) == 2
