'''
Question: Find All Anagrams in a String

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """Find All Anagrams in a String
        Explanation: https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/1738052/A-very-deep-EXPLANATION-oror-Solved-without-using-HashTable

        Args:
            s (str): a string (a-z)
            p (str): a string (a-z)

        Returns:
            List[int]: indices where p appears in s as a anagram
        
        Time complexity:
            Best O(N^2)
            Worst O(N^2)
            where N is the length of s

        Space complexity:
            Best O(N + M)
            Worst O(N + M)
            where N is the length of s and M is the length of p
        """
        n = len(s)
        m = len(p)
        indices = []
        total_chars = 26
        first_char = 97
        # Edge case: phrase is longer than the string
        if n < m:
            return indices
        
        # Initialize the pointers
        start = 0 # start index of the window
        end = start + m - 1 # end index of the window
        
        # Initialize the frequency arrays
        s_freq = [0] * total_chars
        p_freq = [0] * total_chars
        
        # Base case: update frequency for index 0...m-1
        for i in range(start, end + 1):
            s_freq[ord(s[i]) - first_char] += 1
            p_freq[ord(p[i]) - first_char] += 1
        if s_freq == p_freq:
            indices.append(start)
        
        # Increment pointers
        start += 1
        end += 1

        while end < n:
            # Exclude the previous start index character
            s_freq[ord(s[start - 1]) - first_char] -= 1
            # Include the new end index character
            s_freq[ord(s[end]) - first_char] += 1
            if s_freq == p_freq:
                indices.append(start)
            # Increment pointers
            start += 1
            end += 1

        return indices


sol = Solution()
print(sol.findAnagrams("cbaebabacd", "abc"))