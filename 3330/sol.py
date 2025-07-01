from collections import Counter

class Solution:
    def possibleStringCount(self, word: str) -> int:
        """
        Return the total number of possible original strings.
        Only one letter can be reduced at a time.

        Word might be "ere".
        1 <= word.length <= 100
        """
        return 1 + sum(word[i] == word[i - 1] for i in range(1, len(word)))

if __name__ == "__main__":
    sol = Solution()
    word = "abbcccc"
    print(sol.possibleStringCount(word))