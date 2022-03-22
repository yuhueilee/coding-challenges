'''
Question: Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
'''
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        water = 0
        n = len(height)
        i = 0
        j = n - 1
        # Keep track of the max volumn until the two pointers collapse
        while i != j:
            w = j - i
            h = min(height[i], height[j])
            water = max(water, w * h)
            # Move the left pointer if height[i] < height[j] since the
            # volumn obtained from (i, i+1...j) will never exceed (i, j)
            if height[i] < height[j]:
                i += 1
            # Move the right pointer if height[i] >= height[j] since the
            # volumn obtained from (i+1, j) and (i, j-1) are either the same
            # or one is less than the other but will never exceed (i, j)
            else:
                j -= 1
        return water
        
    def maxAreaBruteForce(self, height: List[int]) -> int:
        max_area = 0
        n = len(height)
        for i in range(0, n-1):
            for j in range(1, n):
                h = min(height[i], height[j])
                w = j - i
                area = h * w
                if area > max_area:
                    max_area = area
        return max_area
        