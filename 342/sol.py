class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """
        An integer n is a power of four, if there exists an integer x such that n == 4**x.
        -2**31 <= n <= 2**31 - 1
        """
        # n == 2**2x
        # bin(16)  # '0b10000' have 5 0
        return n > 0 and bin(n).count("1") == 1 and bin(n).count("0") % 2 == 1

if __name__ == "__main__":
    sol = Solution()
    n = 16
    print(sol.isPowerOfFour(n))