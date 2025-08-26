from typing import List

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        """
        Return the area of the rectangle having the longest diagonal.

        1 <= dimensions.length <= 100
        """
        max_d = max_area = 0

        for w, h in dimensions:
            d = w**2 + h**2
            if d > max_d:
                max_d = d
                max_area = w * h
            elif d == max_d:
                max_area = max(max_area, w * h)

        return max_area
    
if __name__ == "__main__":
    sol = Solution()
    dimensions = [[9,3],[8,6]]
    print(sol.areaOfMaxDiagonal(dimensions))