from math import comb

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        """
        Return the total number of ways to distribute n candies among "3" children such that no child gets more than limit candies.
        n = 5, limit = 2
        ways = (1, 2, 2), (2, 1, 2) and (2, 2, 1)
        return 3

        Calculate total ways when one child get more than 1 candies
        1 <= n <= 10**6
        """

        def stars_and_bars_comb(x):
            return comb(x+2, 2) if x >= 0 else 0 

        # Use Stars and Bars to get all ways with no limit.
        # a + b + c = n
        case1 = stars_and_bars_comb(n)

        # One child get more than limit.
        # a > limit, a' >= 0
        # a' = a - (limit + 1)
        # a' + b + c = n - (limit + 1)
        # There are 3 ways that one child get more than limit 
        case2 = 3 * stars_and_bars_comb(n-(limit+1))
        
        # Two children get more than limit.
        # a' + b' + c = n - (limit + 1) * 2
        # There are 3 ways that two child get more than limit 
        case3 = 3 * stars_and_bars_comb(n-(limit+1)*2)
        
        # All children get more than limit.
        # a' + b' + c' = n - (limit + 1) * 3
        case4 = stars_and_bars_comb(n-(limit+1)*3)
        
        # Accroding to inclusion-exclusion principle
        return (case1 - case2 + case3 - case4)
        
if __name__ == "__main__":
    sol = Solution()
    n = 5
    limit = 2
    print(sol.distributeCandies(n, limit))
