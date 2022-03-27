from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """Find the length of the longest increasing subsequence in the lisr

        Args:
            nums (List[int]): a list of integer

        Returns:
            int: length of the LIS
        
        Time complexity:
            Best and Worst O(N^2)
            where N is the length of the input array

        Space complexity:
            Best and Worst O(N)
            where N is the length of the input array
        """
        n = len(nums)
        # Create memo
        memo = [0] * (n + 1)
        
        # Base case
        memo[1] = 1
        
        # Recurrence Relation
        for i in range(2, n + 1):
            length = 1
            for j in range(1, i):
                # Check if it's an increasing sequence
                if nums[j - 1] < nums[i - 1]:
                    # Update the length
                    if memo[j] + 1 > length:
                        length = memo[j] + 1
            # Update memo
            memo[i] = length
        
        max_length = 0
        # Find the maximum length
        for i in range(1, n + 1):
            if memo[i] > max_length:
                max_length = memo[i]
        
        return max_length
                
        