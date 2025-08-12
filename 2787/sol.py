from functools import lru_cache

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        """
        n = n1x + n2x + ... + nkx
        1 <= n <= 300
        1 <= x <= 5
        """
        MOD = 10 ** 9 + 7
        # dp[x] the number of method can compose x
        dp = [0] * (n + 1)
        dp[0] = 1

        k = 1
        while True:
            # print(k, dp)
            power = k ** x
            if power > n:
                break
            
            for j in range(n, power - 1, -1):
                dp[j] = (dp[j] + dp[j - power]) % MOD
        
            k += 1

        return dp[-1]

if __name__ == "__main__":
    sol = Solution()
    n = 36
    x = 1
    print(sol.numberOfWays(n, x))