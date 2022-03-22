import math


class Solution:
    def binaryGap(self, A: int) -> int:
        """Find the maximum binary gap of an integer

        Args:
            A (int): an integer (> 0)

        Returns:
            int: maximum binary gap of the binary representation of the integer

        Time complexity:
            Best and Worst O(logN)
            where N is the integer value

        Space complexity:
            Best and Worst O(logN)
            where N is the integer value
        """
        # Calculate the number of bits to represent the integer
        bits = int(math.log2(A)) + 1
        # Generate all the powers of 2
        power_of_two = [2 ** i for i in range(bits)]
        # Stores all the 1s position
        ones = []
        i = bits - 1
        while A > 0 and i >= 0:
            if power_of_two[i] <= A:
                A -= power_of_two[i]
                ones.append(i)
            i -= 1
        # Calculate the gap between the two consecutive elements
        max_gap = 0
        for i in range(1, len(ones)):
            prev = ones[i - 1]
            curr = ones[i]
            gap = prev - curr - 1
            if gap > max_gap:
                max_gap = gap
        
        return max_gap


sol = Solution()
print(sol.binaryGap(1)) # 1
print(sol.binaryGap(4)) # 100
print(sol.binaryGap(7)) # 111
print(sol.binaryGap(19)) # 10011
