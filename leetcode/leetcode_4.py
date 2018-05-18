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
import numpy as np
import math
import time


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


def find_median_sorted_arrays_np(nums1, nums2):
    sl = np.append(np.sort(nums1), np.sort(nums2))
    return np.median(sl)


t0 = time.time()
answer = find_median_sorted_arrays([1, 2], [3, 4])
t1 = time.time()
print('Standard Python answer:\t', t1-t0, 'Seconds')
print(answer)

t2 = time.time()
answer = find_median_sorted_arrays_np([1, 2], [3, 4])
t3 = time.time()
print('NumPy answer:\t', t3-t2, 'Seconds')
print(answer)
