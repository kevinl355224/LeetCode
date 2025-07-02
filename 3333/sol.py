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

        
if __name__ == "__main__":
    sol = Solution()
    word = "aaaabbbb"
    k = 6
    print(sol.possibleStringCount(word, k))