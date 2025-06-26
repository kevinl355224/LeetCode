class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        """
        Return the length of the longest subsequence of s that makes up a binary number less than or equal to k.
        1 <= s.length <= 1000
        1 <= k <= 10**9
        """
        total = 0
        zeros = s.count("0")
        ones = 0
        power = 1

        for digit in s[::-1]:
            if total + power <= k:
                if digit == "1":
                    total += power
                    ones += 1
                power <<= 1
            else:
                break
        return zeros + ones

if __name__ == "__main__":
    sol = Solution()
    s = "1001010"
    k = 5
    print(sol.longestSubsequence(s, k))