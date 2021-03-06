class Solution:
    def chocolatesByNumber(self, N: int, M: int) -> int:
        """Number of chocolates that you will eat

        Args:
            N (int): a positive integer
            M (int): a positive integer

        Returns:
            int: number of chocolates that you will eat
        
        Time complexity:
            Best O(1)
            Worst O(log(N + M))
            where N is the input integer and M is the input integer

        Space complexity:
            Best and Worst O(1)
        """
        # Edge cases
        if N % M == 0:
            return N // M
        elif N % M == 1:
            return N
        max_divisor = self.gcd(N, M)
        n_factor = N // max_divisor
        m_factor = M // max_divisor

        while max_divisor != 1:
            max_divisor = self.gcd(n_factor, m_factor)
            n_factor = n_factor // max_divisor
            m_factor = m_factor // max_divisor

        return n_factor

    
    def chocolatesByNumberOptimal(self, N: int, M: int) -> int:
        """Number of chocolates that you will eat

        Args:
            N (int): a positive integer
            M (int): a positive integer

        Returns:
            int: number of chocolates that you will eat
        
        Time complexity:
            Best O(1)
            Worst O(log(N + M))
            where N is the input integer and M is the input integer

        Space complexity:
            Best and Worst O(1)
        """
        # Edge cases
        if N % M == 0:
            return N // M
        elif N % M == 1:
            return N
        # Find the least common multiple
        lcm = (N * M) // self.gcd(N, M)

        return lcm // M

    def gcd(self, a: int, b: int) -> int:
        """Find the greatest common divisor between integers a and b

        Args:
            a (int): a positive integer
            b (int): a positive integer

        Returns:
            int: greatest common divisor

        Time complexity:
            Best and Worst O(a + b)
            where a is the input integer and b is the input integer
        
        Space complexity:
            Best and Worst O(1)
        """
        if a == b:
            return a
        elif a > b:
            return self.gcd(a - b, b)
        elif a < b:
            return self.gcd(a, b - a)


sol = Solution()
print(sol.chocolatesByNumberOptimal(10, 4))