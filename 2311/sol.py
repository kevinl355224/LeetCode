class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        """
        Return the length of the longest subsequence of s that makes up a binary number less than or equal to k.
        1 <= s.length <= 1000
        1 <= k <= 10**9
        """
        total = 0
        base = 1
        cnt = 0
        for digit in s[::-1]:
            if total + base <= k:
                if int(digit):
                    total += base
                base *= 2
                cnt += 1
            else:
                if digit == "0":
                    cnt += 1     
        return cnt

if __name__ == "__main__":
    sol = Solution()
    s = "1001010"
    k = 5
    print(sol.longestSubsequence(s, k))