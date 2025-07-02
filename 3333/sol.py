class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        """
        Return the total number of possible original strings that size at least k.

        Word might be "ere".
        len(word) >= k

        1 <= word.length <= 5 * 10**5
        1 <= k <= 2000
        """
        MOD = 10**9 + 7

        # Break down words into groups num of word etc. "abbccc" -> [1, 2, 3]
        groups = []
        count = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count)

        # All possible combination without consider k.
        total = 1
        for num in groups:
            total = (total * num) % MOD

        if k < len(groups):
            return total

        # Init dp
        # dp[s] means: the number of ways to keep exactly s characters in the original string.
        # dp = [1,0,0,0...]
        dp = [0] * k
        dp[0] = 1
        """
        ex: word = "aabbccdd"
        groups = [2, 2, 2, 2]

        At this point, dp[s] represents the number of ways to keep exactly s characters so far.

        When processing a group of length 2 (e.g., the 'c' group),
        to keep exactly 2 characters, we sum dp[s - x] for x in [1..2],
        meaning we add the ways to keep (2-1)=1 or (2-2)=0 characters from previous groups,
        and keep x characters from the current group,
        forming subsequences of length 2 in total.
        """
        for num in groups:
            new_dp = [0] * k
            sum_value = 0
            for i in range(1, k):
                # Sliding window
                sum_value = (sum_value + dp [i - 1]) % MOD
                if i > num:
                    sum_value = (sum_value - dp[i - num - 1] + MOD) % MOD
                new_dp[i] = sum_value
            dp = new_dp

        invalid = sum(dp[len(groups):k]) % MOD
        return (total - invalid + MOD) % MOD
    
if __name__ == "__main__":
    sol = Solution()
    word = "aabbccdd"
    k = 7
    print(sol.possibleStringCount(word, k))