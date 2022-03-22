'''
Question: Combination Sum

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example:
    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]
    Explanation:
        2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
        7 is a candidate, and 7 = 7.
        These are the only two combinations.
'''
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [] # all completed and valid combinations
        path = [] # current potential combination
        index = 0 # index of the candidates list
        candidates.sort() # sort the list for early termination of recursion
        self.dfs(candidates, target, index, path, res)
        return res
    
    def dfs(self, nums, target, index, path, res):
        if target == 0:
            res.append(path)
            return 
        for i in range(index, len(nums)):
            # early termination for the loop and recursion
            if target - nums[i] < 0:  
                break
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res) 