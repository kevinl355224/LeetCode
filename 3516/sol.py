from typing import List

class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        """
        Both x and Person y move toward z at the same speed.
        Determine which person reaches z first:

        Return 1 if x arrives first.
        Return 2 if y arrives first.
        Return 0 if both arrive at the same time.
        """
        return 1 if abs(z - x) < abs(z - y) else (2 if abs(z - y) < abs(z - x) else 0)

    
if __name__ == "__main__":
    sol = Solution()
    x = 2
    y = 7
    z = 4
    print(sol.findClosest(x, y, z))