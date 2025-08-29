from typing import List

class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # Try cnt odd pairs
        return ((n + 1) // 2) * (m // 2) + (n // 2) * ((m + 1) // 2)



if __name__ == "__main__":
    sol = Solution()
    n = 3
    m = 2
    print(sol.flowerGame(n, m))