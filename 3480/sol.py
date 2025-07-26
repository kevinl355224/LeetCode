from typing import List

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        """
        Remove exactly one element from conflictingPairs [a, b].
        Afterward, count the number of non-empty subarrays of nums.
        Which do not contain both a and b for any remaining conflicting pair [a, b].

        Return the maximum number of subarrays possible after removing.

        2 <= n <= 10**5
        1 <= conflictingPairs.length <= 2 * n
        """

if __name__ == "__main__":
    sol = Solution()
    n = 4
    conflictingPairs = [[2,3],[1,4]]
    print(sol.maxSubarrays(n, conflictingPairs))