class Solution:
    def numTilings(self, n: int) -> int:
        # dp[i] = Ways to cover i column, both rows of column i are covered.
        # dp2[i] = Ways to cover i column, top or bottom row of column i are covered.
        # If there have different shape of domino, we should assume more status like dp3, dp4, dp5....

        # dp[0] = 1
        # dp[1] = 1 
        # dp[2] = 2 // dp2[2] = 1 Put one tormino on i-1 will let i column have a top or bottom column covered  

        # dp[i] = dp[i-1] + dp[i-2] + 2dp2[i-1]
        # dp2[i] = dp[i-2] + dp2[i-1] 

        # i = 3 ANS = 5
        # dp[3] = dp[2] + dp[1] + dp2[2]*2 = 5 <-- Answer
        # dp2[3] = dp[1] + dp2[2] = 2

        # i = 4 ANS = 11
        # dp[4] = dp[3] + dp[2] + dp2[3]*2 = 5 + 2 + 2*2 = 11 <-- Answer
        # dp2[4] = dp[2] + dp2[3] = 4

        # Initialize
        MOD = 10**9 + 7
        dp = [0]*(n+1) # dp[0] is 0 column. So i column have n+1 array.
        dp2 = [0]*(n+1)
        print(dp)

        dp[0], dp[1], dp[2] = 1, 1, 2
        dp2[0], dp2[1], dp2[2] = 0, 0, 1

        if n == 0:
            return 1
        elif n == 1:
            return 1
        elif n == 2:
            return 2

        for i in range(3, n+1): # The ans is i row dp[i]
            dp[i] = (dp[i-1] + dp[i-2] + 2*dp2[i-1]) % MOD
            dp2[i] = (dp[i-2] + dp2[i-1]) % MOD
            print(i)
            print(dp)

        print(dp[n])
        return dp[n]

if __name__ == "__main__":
    sol = Solution()
    print(sol.numTilings(4))