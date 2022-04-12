from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """Find the median of the two sorted arrays

        Args:
            nums1 (List[int]): a sorted integer list
            nums2 (List[int]): a sorted integer list

        Returns:
            float: median of the two sorted arrays
        
        Time complexity:
            Best O(log(M+N))
            Worst O(log(M+N))
            where M is the length of nums1 and N is the length of nums2

        Space complexity:
            Best and Worst O(1)
        """
        m = len(nums1)
        n = len(nums2)
        
        # Calculate the median index
        indexes = []
        if (m + n) % 2 == 0:
            indexes.append((m + n) // 2 - 1)
        indexes.append((m + n) // 2)
        
        # Create two pointers for the two arrays
        i, j = 0, 0
        index = -1
        medians = []
        
        # Find the element corresponds to the median index
        while index < indexes[-1]:
            # Indicate whether pointer i is increased
            increaseI = False
            if i < m:
                # Increment i if nums1 element is less than nums2
                # or if j reached the end of nums2
                if j == n or nums1[i] <= nums2[j]:
                    i += 1
                    increaseI = True
                elif nums1[i] > nums2[j] and j < n:
                    j += 1
            # Increment j if i reached the end of nums1
            elif j < n:
                j += 1
            # Increment index
            index += 1
            
            if index in indexes:
                median = nums1[i-1] if increaseI else nums2[j-1]
                medians.append(median)
                
        if len(medians) == 1:
            return medians[0]
        
        return sum(medians) / 2