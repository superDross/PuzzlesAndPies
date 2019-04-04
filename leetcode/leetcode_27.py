''' 27 - Remove Element

Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
'''


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if val == nums[i]:
                nums.pop(i)
            else:
                i += 1
        if i == 0:
            if not nums:
                return 0
            return nums
        return len(nums)


nums, val = ([3, 2, 2, 3], 3)
nums, val = ([0, 1, 2, 2, 3, 0, 4, 2], 2)
nums, val = ([1], 1)

print(Solution().removeElement(nums, val))
