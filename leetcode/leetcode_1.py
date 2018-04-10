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
import numpy as np
import time


def two_sum(nums, target):
    ''' You build the dict on an needed basis'''
    lookup = {}
    for i, n in enumerate(nums):
        if n in lookup:
            return [lookup[n], i]
        else:
            # I don't understand target - n
            lookup[target - n] = i


def two_sum_brute(nums, target):
    r = range(0, len(nums))
    for i in r:
        for j in r:
            if nums[i] + nums[j] == target and i != j:
                return [i, j]


def two_sum_np(nums, target):
    nums = np.array(nums)
    vstack = nums[:, np.newaxis]
    combinations = nums + vstack
    indexes = np.where(combinations == target)[0]
    return indexes


nums = [2, 7, 11, 15]
target = 17
t0 = time.time()
answer = two_sum(nums, target)
t1 = time.time()
print(t1 - t0)
print(answer)
