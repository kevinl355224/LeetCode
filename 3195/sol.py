from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        """
         Find a rectangle with horizontal and vertical sides with the smallest area, 
         such that all the 1's in grid lie inside this rectangle.

        1 <= grid.length, grid[i].length <= 1000
        """
        height = [float("inf"), -1] # Top and bottom
        width = [float("inf"), -1] # Left and right
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    # Update list
                    if width[0] > col:
                        width[0] = col
                    if width[1] < col:
                        width[1] = col
                    if height[0] > row:
                        height[0] = row
                    if height[1] < row:
                        height[1] = row
        return (height[1] - height[0] + 1) * (width[1] - width[0] + 1)


if __name__ == "__main__":
    sol = Solution()
    grid = [[1,0],[0,0]]
    print(sol.minimumArea(grid))