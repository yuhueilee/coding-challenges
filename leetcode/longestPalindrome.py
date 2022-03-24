class Solution:
    def longestPalindrome(self, s: str) -> str:
        """Given a string s, return the longest palindromic substring in s

        Args:
            s (str): a string

        Returns:
            str: longest palindrome in string
        
        Time complexity:
            Best and Worst O(N^2)
            where N is the length of the input string

        Space complexity:
            Best and Worst O(N)
            where N is the length of the input string
        """
        n = len(s)
        mid_lengths = [1, 2] # minimum length of the palindrome - odd or even length
        max_length = 1 # maximum length of palindrome
        left = 0 # leftmost index of the palindrome
        right = 0 # rightmost index of the palindrome
        
        for mid_length in mid_lengths:
            # Odd length - [0, 1, 2, ..., n-1]
            # Even length - [0, 1, 2, ..., n-2]
            mid_points = [i for i in range(0, n - mid_length + 1)]
            for mid_point in mid_points:
                start = 0 # start index
                end = 0 # end index
                length = 0
                # Odd length palindrome
                if mid_length == 1:
                    start = mid_point - 1
                    end = mid_point + 1
                    length = 1 # a single letter is a palindrome of length 1
                # Even length palindrome
                elif mid_length == 2:
                    start = mid_point
                    end = mid_point + 1
                # Find the maximum length of the palindrome with the mid point
                length, start, end = self.lengthOfPalindrome(s, start, end, length)
                # Update the maximum length
                if length > max_length:
                    max_length = length
                    left = start
                    right = end
        return s[left:right+1]
        
    def lengthOfPalindrome(self, s: str, start: int, end: int, length: int):
        """Recursively find the length of the palidrome by comparing letters 
        at start and end index, if same then increment length by 2

        Args:
            s (str): a string
            start (int): start index
            end (int): end index
            length (int): current length of the valid palindrome

        Returns:
            (int, int, int): length, start index, end index
        
        Time complexity:
            Best and Worst O(N/2)
            where N is the length of the input string

        Space complexity:
            Best and Worst O(1)
        """
        # Base case: invalid boundary
        if start < 0 or end > len(s) - 1:
            # return previous valid length and indexes
            return (length, start + 1, end - 1)
        elif s[start] != s[end]:
            # return previous valid length and indexes
            return (length, start + 1, end - 1)
        elif s[start] == s[end]:
            return self.lengthOfPalindrome(s, start - 1, end + 1, length + 2)


sol = Solution()
print(sol.longestPalindrome("aa"))