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
            Best and Worst O(N + M)
            where N is the integer value and M is the length of the array

        Space complexity:
            Best and Worst O(N + M)
            where N is the integer value and M is the length of the array
        """
        counter = [0] * N
        max_counter = 0 # store the max counter value used in the max counter operation
        max_val = 0 # store the max value among the current counter

        for k in range(len(A)):
            if A[k] == N + 1:
                # assign max value to max counter
                max_counter = max_val
            elif 1 <= A[k] <= N:
                # check if max counter operation is performed previously
                if max_counter > 0:
                    # check if the counter value has been up-to-date
                    if counter[A[k] - 1] >= max_counter:
                        counter[A[k] - 1] += 1
                    elif counter[A[k] - 1] < max_counter:
                        counter[A[k] - 1] = 1 + max_counter
                # normal increase by 1 operation
                elif max_counter == 0:
                    counter[A[k] - 1] += 1
                # update max value
                if counter[A[k] - 1] > max_val:
                    max_val = counter[A[k] - 1]

        # update all the counter
        if max_counter > 0:
            for i in range(len(counter)):
                if counter[i] < max_counter:
                    counter[i] = max_counter

        return counter

    def maxCountersNaive(self, N: int, A: List[int]) -> List[int]:
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
print(sol.maxCountersNaive(5, [3, 4, 4, 6, 1, 4, 4]))
print(sol.maxCountersNaive(2, [1, 1, 1, 1, 1, 1, 1]))
print(sol.maxCounters(5, [3, 4, 4, 6, 1, 4, 4]))
print(sol.maxCounters(2, [1, 1, 1, 1, 1, 1, 1]))
