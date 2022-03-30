from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """Find repeated DNA sequence in the input string

        Args:
            s (str): a string (ATCG)

        Returns:
            List[str]: a list of repeated DNA sequence
        
        Time complexity:
            Best and Worst O(N^2)
            where N is the length of the input string

        Space complexity:
            Best and Worst O(N^2)
            where N is the length of the input string
        """
        n = len(s)
        
        # Create z arrays for all the suffixes of length >= 10
        z_arrs = []
        i = 0
        while i <= n - 10:
            z_arr = self.computeZValues(s[i:])
            z_arrs.append(z_arr)
            i += 1
        
        # Find index where z_arr[i] >= 10
        res = []
        for k in range(len(z_arrs)):
            z_arr = z_arrs[k]
            i = 1
            while i < len(z_arr):
                if z_arr[i] >= 10:
                    start = k + i
                    end = start + 10
                    if s[start:end] not in res:
                        res.append(s[start:end])
                i += 1
        
        return res
        
        
    def computeZValues(self, string: str):
        """Dynamically compute the z-values of the input string

        Args:
            string (str): a string

        Returns:
            (List[int]): a list of numbers shows the longest matching 
            substring (with the prefix) started at that index

        Time complexity:
            Best case: O(N)
            Worst case: O(N)

            where N is the length of the input string
        """
        n = len(string)
        z_array = [0] * n
        z_array[0] = n
        # initialize the left and right pointer
        left, right = 0, 0
        # placeholder to store the longest matching substring
        num_of_matches = 0
        for i in range(1, n):
            # case 1: i is outside of z-box
            if i > right:
                num_of_matches = self.compare(string, 0, i)
                z_array[i] = num_of_matches
                left, right = self.updateZBox(i, left, right, num_of_matches)
            else:
                k = i - left
                remaining = right - i + 1
                # case 2a
                if z_array[k] < remaining:
                    z_array[i] = z_array[k]
                # case 2b
                elif z_array[k] > remaining:
                    z_array[i] = remaining
                # case 2c
                else:
                    # compare string[right+1:n]
                    num_of_matches = self.compare(string, right + 1 - i, right + 1)
                    z_array[i] = z_array[k] + num_of_matches
                    left, right = self.updateZBox(i, left, right, num_of_matches)
        return z_array

    def updateZBox(self, curr: int, l: int, r: int, num_of_matches: int):
        """Update the left and right pointer of the z-box
        given the current index and the number of matching 
        substring (starting at curr index) with the prefix

        Args:
            curr (int): current index
            l (int): left pointer of the z-box
            r (int): right pointer of the z-box
            num_of_matches (int): number of matching character of the substring
            with the prefix

        Returns:
            (int, int): new left and right pointer of the z-box
        """
        left, right = l, r
        if num_of_matches > 0:
            left = curr
            right = curr + num_of_matches - 1
        return left, right

    def compare(self, string: str, x: int, y: int):
        """Compare the string and the substring and count the 
        number of matches characters

        Args:
            string (str): a string
            x (int): a number represents the start index of the string
            y (int): a number represents the start index of the substring

        Returns:
            (int): number of matches between string 
            and substring
        Time complexity:
            Best case: O(1) when the two string are different at the first character
            Worst case: O(M) where M is the number of matches between string and substring
        """
        num_of_matches = 0
        n = len(string)
        i, j = x, y
        while j < n and string[i] == string[j]:
            num_of_matches += 1
            i += 1
            j += 1
        return num_of_matches


sol = Solution()
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTTAAAAACCCCC"
print(sol.findRepeatedDnaSequences(s))
s = "AAAAAAAAAAAAA"
print(sol.findRepeatedDnaSequences(s))