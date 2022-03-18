'''
Question: Subsets

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nth_bit = 1 << n # 1 * (2 ** n)
        combinations = []
        for i in range(2** n):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i | nth_bit)[3:]
            comb = [nums[i] for i in range(len(bitmask)) if int(bitmask[i]) == 1]
            combinations.append(comb)
        return combinations
        

sol = Solution()
print(sol.subsets([1, 2, 3]))
