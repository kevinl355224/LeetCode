class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        """
        Alice starts with 0 points and draws numbers while she has less than k points.
        Alice stops drawing numbers when she gets k or more points.

        Return the probability that Alice has n or fewer points.
        Answers within 10**-5 of the actual answer are considered accepted.

        1 <= maxPts <= 10**4
        0 <= k <= n <= 10**4
        """

        dp = [0] * (n + 1)  # The probability can get specific score.
        dp[0] = 1
        window_sum = 1.0 # sum of last maxPts dp values

        #　Draw card if 
        
        for i in range(1, n + 1):
            dp[i] = window_sum / maxPts
            if i < k:
                window_sum += dp[i]
            if i - maxPts >= 0:
                window_sum -= dp[i - maxPts]

        return round(sum(dp[k:]), 5)


if __name__ == "__main__":
    sol = Solution()
    n = 21
    k = 17
    maxPts = 10
    print(sol.new21Game(n, k, maxPts))