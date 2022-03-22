'''
Question: Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
'''
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """Find the start and end index of the target in nums (sorted, ascending) array.

        Args:
            nums (List[int]): a list of integers (incl. positive and negative)
            target (int): an integer

        Returns:
            List[int]: start and end index
        
        Time complexity:
            Best O(logN) for binary search
            Worst O(logN) for binary search
            where N is the number of elements in the nums array

        Space complexity:
            Best O(N) for the input array
            Worst O(N) for the input array
            where N is the number of elements in the nums array
        """
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
                # terminate recursion when reaching the mid pointer reaches the edge of array
                if mid == left:
                    return mid
                else:
                    # memorize the last found target index
                    lastest_index = mid
                    # continue recursion to the left side to ensure no other target exists
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
                # terminate recursion when reaching the mid pointer reaches the edge of array
                if mid == right:
                    return mid
                else:
                    # memorize the last found target index
                    lastest_index = mid
                    # continue recursion to the right side to ensure no other target exists
                    return self.findEnd(nums, target, mid + 1, right, lastest_index)
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
            return self.findEnd(nums, target, left, right, lastest_index)
        else:
            return lastest_index