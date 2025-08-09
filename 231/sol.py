class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        "-231 <= n <= 231 - 1"
        return n > 0 and bin(n).count("1") == 1
        

if __name__ == "__main__":
    sol = Solution()
    n = 16
    print(sol.isPowerOfTwo(n))
