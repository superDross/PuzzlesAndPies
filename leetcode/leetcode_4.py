''' LeetCode 4 - Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''
import math


def find_median_sorted_arrays(nums1, nums2):
    sl = sorted(nums1 + nums2)
    # round up if at 0.5
    i = math.ceil(len(sl) / 2)
    # even number lists
    if len(sl) % 2 == 0:
        median = (sl[i - 1] + sl[i]) / 2
    else:
        median = sl[i - 1]
    return median


answer = find_median_sorted_arrays([1, 2], [3, 4])
print(answer)
