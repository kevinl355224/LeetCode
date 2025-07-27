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
        # Calculate the number of valid subarrays that end at position r, for r from 1 to n.
        
        # Use right to save all `a` for `b`.
        right = [[] for _ in range(n + 1)]
        for a, b in conflictingPairs:
            right[max(a, b)].append(min(a, b))
        
        # Number of valid subarrays without removing any pair.
        base = 0

        left = [0, 0] # Save the top two `a` for edge `b`
        bonus = [0] * (n + 1)
        for r in range(1, n + 1):
            for l in right[r]:
                if l > left[0]:
                    left = [l, left[0]]
                elif l > left[1]:
                    left = [left[0], l]
            # Caculate `base`
            """
            If r = 5, left[0] = 3
            Valid subarrays end with `5` is [4,5], [5,5]
            """
            base += r - left[0]

            # Caculate `bonus`
            """
            r and all subarray
            1. [1,1]
            2. [1,2], [2,2]
            3. [1,3], [2,3], [3,3]
            4. [1,4], [2,4], [3,4], [4,4]

            conflictPairs = [2,3], [1,4]
            [1,4] affect [1,4] 
            [2,3] affect [1,3], [2,3], [2,4]

            r = 3, left = [2,0]
            bonus[2] = 0 + 2 - 0
            r = 4, left = [2,1]
            bonus[2] = 2 + 2 - 1
            """
            if left[0] > 0:
                bonus[left[0]] += left[0] - left[1]
        # print(bonus)
        return base + max(bonus)

if __name__ == "__main__":
    sol = Solution()
    n = 4
    conflictingPairs = [[2,3],[1,4]]
    print(sol.maxSubarrays(n, conflictingPairs))
