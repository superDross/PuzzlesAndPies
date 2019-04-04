''' 26 - Remove Duplicate from a Sorted Array

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i = 1
        while i < len(nums):
            if nums[i-1] == nums[i]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)


nums = [1, 1, 2]
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
Solution().removeDuplicates(nums)
