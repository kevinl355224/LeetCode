class Solution:
    def kthCharacter(self, k: int) -> str:
        """
        Start with letter "a"
        Generate next character in the English alphabet, and append it to the original word.
        Return the value of the kth character in word

        ex. "a" -> "a" + "b", "ab" -> "ab" + "bc"...
        1 <= k <= 500
        """

        """
        (5).bit_count() = 0b101 → 2
        (8).bit_count() = 0b1000 → 1
        (15).bit_count() = 0b1111 → 4
        """
        return chr(ord('a') + (k - 1).bit_count())


if __name__ == "__main__":
    sol = Solution()
    k = 16
    print(sol.kthCharacter(k))