from typing import List

# Incomplete Solution
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0 # start index
        j = len(nums) - 1 # end index
        k = i + 1 # mid index
        
        # Sort the nums array
        nums.sort()
        
        res = []
        
        # Record the previous sums
        if i < k < j:
            prev_sum = nums[i] + nums[j] + nums[k]
        
        # Iterate through the sorted array by incrementing i
        # or decrementing j while i < k < j
        while i < k and k < j:
            curr_sum = nums[i] + nums[j] + nums[k]
            # Case 1: sum is exactly zero
            if curr_sum == 0:
                sol = [nums[i], nums[j], nums[k]]
                if sol not in res:
                    res.append(sol)
                # Sum is too big without nums[k]
                if curr_sum - nums[k] > 0:
                    k -= 1
                # Sum is too small or not affected by nums[k]
                elif curr_sum - nums[k] <= 0:
                    k += 1
                # Assign to prev sum
                prev_sum = curr_sum
            # Case 2: sum is too big
            elif curr_sum > 0:
                # From too big to too big
                if prev_sum > 0:
                    k -= 1
                    # Assign to prev sum
                    prev_sum = curr_sum
                # From too small or exactly zero to too big
                elif prev_sum <= 0:
                    # Exclude the right end element
                    j -= 1
                    k = i + 1
                    prev_sum = nums[i] + nums[j] + nums[k]
            # Case 3: sum is too small
            elif curr_sum < 0:
                # From too small to too small
                if prev_sum < 0:
                    k += 1
                    # Assign to prev sum
                    prev_sum = curr_sum
                # From too big or exactly zero to too small
                elif prev_sum >= 0:
                    # Exclude the left end element
                    i += 1
                    k = i + 1
                    prev_sum = nums[i] + nums[j] + nums[k]

            # Update pointers and reset prev sum
            if k == i:
                j -= 1
                k += 1
                prev_sum = nums[i] + nums[j] + nums[k]
            elif k == j:
                i += 1
                k -= 1
                prev_sum = nums[i] + nums[j] + nums[k]
        
        return res
        

sol = Solution()
print(sol.threeSum([-2,0,1,1,2])) 
print(sol.threeSum([-1,1,-2,-1]))
print(sol.threeSum([-1,0,1,2,-1,-4]))
print(sol.threeSum([]))
print(sol.threeSum([0]))
print(sol.threeSum([0,0]))
print(sol.threeSum([1,-1]))