'''
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
'''
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = -1, -1
        # find the first index of target in nums array
        index = self.binarySearch(nums, target, 0, len(nums) - 1)
        if index == -1:
            return [start, end]
        # find the start and end position of target in nums array
        start = self.findStart(nums, target, 0, index - 1, index)
        end = self.findEnd(nums, target, index + 1, len(nums) - 1, index)

        return [start, end]
        
    def binarySearch(self, nums, target, left, right):
        if left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
            return self.binarySearch(nums, target, left, right)
        else:
            return -1
    
    def findStart(self, nums, target, left, right, lastest_index):
        if left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                if mid == left:
                    return mid
                else:
                    lastest_index = mid
                    return self.findStart(nums, target, left, mid - 1, lastest_index)
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
            return self.findStart(nums, target, left, right, lastest_index)
        else:
            return lastest_index
        
    def findEnd(self, nums, target, left, right, lastest_index):
        if left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                if mid == right:
                    return mid
                else:
                    lastest_index = mid
                    return self.findEnd(nums, target, mid + 1, right, lastest_index)
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
            return self.findEnd(nums, target, left, right, lastest_index)
        else:
            return lastest_index