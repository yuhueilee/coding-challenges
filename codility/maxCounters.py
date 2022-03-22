from typing import List


class Solution:
    def maxCounters(self, N: int, A: List[int]) -> List[int]:
      """Given an integer N and a non-empty array A consisting of M integers, 
      returns a sequence of integers representing the values of the counters

      Args:
          N (int): a positive integer
          A (List[int]): an array of positive integers

      Returns:
          List[int]: counter
        
      Time complexity:
            Best and Worst O(NM)
            where N is the integer value and M is the length of the array

      Space complexity:
          Best and Worst O(NM)
          where N is the integer value and M is the length of the array
      """
      counter = [0] * N
      for k in range(len(A)):
          if A[k] == N + 1:
              max_counter = max(counter)
              counter = [max_counter for _ in range(N)]
          elif 1 <= A[k] <= N:
              counter[A[k] - 1] += 1
      
      return counter


sol = Solution()
print(sol.maxCounters(5, [3, 4, 4, 6, 1, 4, 4]))
print(sol.maxCounters(2, [1, 1, 1, 1, 1, 1, 1]))
