class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """
        -231 <= n <= 231 - 1
        """
        if n <= 0:
            return False
        power = 1
        while power <= n:
            if power == n:
                return True
            power *= 3
        return False

if __name__ == "__main__":
    sol = Solution()
    n = 3
    print(sol.isPowerOfThree(n))