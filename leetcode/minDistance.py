class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """Given two strings word1 and word2, return the 
        minimum number of operations required to convert word1 to word2

        Args:
            word1 (str): a string
            word2 (str): a string

        Returns:
            int: minimum edit distance

        Time complexity:
            Best and Worst O(MN)
            where M is the length of word1 and N is the length of word2

        Space complexity:
            Best and Worst O(MN)
            where M is the length of word1 and N is the length of word2
        """
        m = len(word1)
        n = len(word2)
        
        # Create memo
        memo = [None] * n
        for i in range(n):
            memo[i] = [0] * m
        
        # Edge cases
        if m == 0 and n == 0:
            return 0
        elif m == 0:
            return n
        elif n == 0:
            return m
        
        # Base case 1: convert one character to one character
        if word1[0] != word2[0]:
            memo[0][0] = 1 # replace operation
        elif word1[0] == word2[0]:
            memo[0][0] = 0 # no operation
        
        # Base case 2: convert j characters to one character
        for j in range(1, m):
            if word1[j] != word2[0]:
                memo[0][j] = memo[0][j-1] + 1 # delete operation
            elif word1[j] == word2[0]:
                memo[0][j] = j # delete operation j times
        
        # Base case 2: convert one character to i characters
        for i in range(1, n):
            if word1[0] != word2[i]:
                memo[i][0] = memo[i-1][0] + 1 # insert operation
            elif word1[0] == word2[i]:
                memo[i][0] = i # insert operation i times
                
        # Recurrence relation
        for i in range(1, n):
            for j in range(1, m):
                # Case 1: same character
                if word1[j] == word2[i]:
                    memo[i][j] = memo[i-1][j-1]
                # Case 2: diff character
                elif word1[j] != word2[i]:
                    memo[i][j] = min(
                        memo[i-1][j-1], # followed by replace
                        memo[i-1][j],   # followed by delete
                        memo[i][j-1],   # followed by insert
                    ) + 1
        
        return memo[n-1][m-1]
        
        
sol = Solution()
print(sol.minDistance(word1 = "horse", word2 = "ros"))
print(sol.minDistance(word1 = "sea", word2 = "eat"))