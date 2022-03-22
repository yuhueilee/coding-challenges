'''
Question: Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
'''
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        distinct = 0
        replace = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[distinct]:
                distinct = i
                k += 1
                nums[replace] = nums[i]
                replace += 1
        
        return k
        