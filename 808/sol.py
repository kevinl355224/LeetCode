import math
from functools import lru_cache

class Solution:
    def soupServings(self, n: int) -> float:
        """
        soupA, soupB = n
        P(soupA used up first) + 0.5 * P(soupA, soupB used up same time)
        Four kind of operation:
            soupA: 100 | soupB:  0
            soupA:  75 | soupB: 25
            soupA:  50 | soupB: 50
            soupA:  25 | soupB: 75

        0 <= n <= 10**9
        """
        # Answers within 10**-5 of the actual answer will be accepted.
        if n > 5000: return 1

        units = math.ceil(n / 25)

        @lru_cache
        def dfs(soupA, soupB):
            if soupA <= 0 and soupB <= 0:
                return 0.5
            if soupA <= 0:
                return 1
            if soupB <= 0:
                return 0
            
            return 0.25 * (
                dfs(soupA - 4, soupB) +
                dfs(soupA - 3, soupB - 1) +
                dfs(soupA - 2, soupB - 2) +
                dfs(soupA - 1, soupB - 3) 
            )

        return dfs(units, units)

if __name__ == "__main__" :
    sol = Solution()
    n = 50
    print(sol.soupServings(n))