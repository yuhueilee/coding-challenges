class Solution:
    def climbStairs(self, n: int) -> int:
        """Return the number of possible ways to climb n stairs provided that
        each time can climb 1 or 2 stair case

        Args:
            n (int): number of stairs

        Returns:
            int: number of possible ways
        
        Time complexity:
            Best and Worst O(N)
            where N is the input number
        
        Space complexity:
            Best and Worst O(N)
            where N is the input number
        """
        memo = [0] * (n+1)
        # Base case
        memo[0] = 1 # 1 combination for climbing 0 stair
        memo[1] = 1 # 1 combination for climbing 1 stair
        
        for i in range(2, n+1):
            memo[i] = memo[i-1] + memo[i-2]
        
        return memo[n]
    
    def climbStairsVer2(self, n: int) -> int:
        """Return the number of possible ways to climb n stairs provided that
        each time can climb 1, 2 or 3 stair case

        Args:
            n (int): number of stairs

        Returns:
            int: number of possible ways
        
        Time complexity:
            Best and Worst O(N)
            where N is the input number
        
        Space complexity:
            Best and Worst O(N)
            where N is the input number
        """
        memo = [0] * (n + 1)
        # Base case
        memo[0] = 1
        memo[1] = 1
        # Recurrence relation
        for i in range(2, n+1):
            ways = 0
            if i - 1 >= 0:
                ways += memo[i-1]
                if i - 2 >= 0:
                    ways += memo[i-2]
                    if i - 3 >= 0:
                        ways += memo[i-3]
            memo[i] = ways
        
        return memo[n]

sol = Solution()
print(sol.climbStairsVer2(6))