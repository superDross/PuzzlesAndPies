''' LeetCode 35 - Search Insert Position 

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2

Example 2:

Input: [1,3,5,6], 2
Output: 1

Example 3:

Input: [1,3,5,6], 7
Output: 4

Example 4:

Input: [1,3,5,6], 0
Output: 0

'''


def searchInsert(nums, target):
    ''' Modified version of the binary search algorithm.'''
    index_counter = 0
    nums.sort()
    while True:
        i = len(nums)//2
        centre = nums[i]
        if centre == target:
            return index_counter+i
        elif len(nums) == 1 and centre == target:
            return index_counter
        elif len(nums) == 1:
            if target > centre:
                return index_counter+1
            else:
                return index_counter
        elif centre < target:
            nums = nums[i:]
            index_counter += len(nums[:i])
        else:
            nums = nums[:i]
            index_counter += len(nums[i:])


assert searchInsert([1, 3, 5, 6], 5) == 2
assert searchInsert([1, 3, 5, 6], 6) == 3
assert searchInsert([1, 3, 5, 6, 12, 90, 26, 10, 99, 89, 388], 10) == 4
assert searchInsert([1, 3, 5, 6], 2) == 1
assert searchInsert([1, 3, 5, 6], 7) == 4
assert searchInsert([2, 5], 1) == 0
