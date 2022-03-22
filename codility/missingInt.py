from typing import List


class Solution:
    def missingInt(self, A: List[int]) -> int:
        """Find the smallest positive integer in the array (that is greater than 0)

        Args:
            A (List[int]): an array of integers (length >= 1)

        Returns:
            int: smallest positive integer missing in the input array

        Time complexity:
            Best and Worst O(N)
            where N is the length of the input array
        
        Space complexity:
            Best and Worst O(N)
            where N is the length of the input array
        """
        A.sort()
        N = len(A)
        min_int = 1
        found = False
        i = 1
        while i < N and not found:
            prev = A[i - 1]
            curr = A[i]
            # Edge case
            if i - 1 == 0 and prev > 1:
                found = True
                min_int = 1
            # Gap found
            elif curr - prev > 1:
                # Both are positive and has a difference more than 1
                if curr > 0 and prev > 0:
                    found = True 
                    min_int = prev + 1
                # Only curr is positive and more than 1
                elif curr > 1 and prev <= 0:
                    found = True
                    min_int = 1
            i += 1
        
        # Edge case
        if not found:
            # Check if the last element is postive
            if A[N - 1] > 0:
                # Check if the first element is not 1
                if A[0] > 1:
                    min_int = 1
                else:
                    min_int = A[N - 1] + 1
            elif A[N - 1] <= 0:
                min_int = 1

        return min_int


sol = Solution()
print(sol.missingInt([1,1,-3,0,2,4]))
print(sol.missingInt([0,0,0,0]))
print(sol.missingInt([2,4,6,8]))
print(sol.missingInt([2]))
print(sol.missingInt([-1]))
print(sol.missingInt([1, 2, 3, 1, 2, 3, -1, 1000000]))