from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # [1,2,34,3,4,5,7,23,12]
        # [5,7,23]
        # If 3 consecutive odd return true, Otherwise return false.
        # Try find every three digit is odd, then check the adjacent digit.

        for i in range(len(arr)-2):
            if arr[i] % 2 == 1 and arr[i+1] % 2 == 1 and arr[i+2] % 2 == 1:
                return True
        return False

if __name__ == "__main__":
    arr = [1,2,34,3,4,5,7,23,12]
    sol = Solution()
    print(sol.threeConsecutiveOdds(arr))