from typing import List

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        res = float("inf")
        # Rotate 4 times
        for _ in range(4):
            n, m = len(grid), len(grid[0])
            # First cut: split the grid horizontally into two parts
            for i in range(1, n):
                a1 = self.minimumgridrea(grid[:i]) # top part (first rectangle)
                # Second cut option 1: split the bottom part vertically into two rectangles
                for j in range(1, m):
                    part2 = [row[:j] for row in grid[i:]] # bottom-left rectangle
                    part3 = [row[j:] for row in grid[i:]] # bottom-right rectangle
                    a2 = self.minimumgridrea(part2)
                    a3 = self.minimumgridrea(part3)
                    res = min(res, a1 + a2 + a3)
                # Second cut option 2: split the bottom part horizontally again
                for i2 in range(i + 1, n):
                    part2 = grid[i:i2]  # middle rectangle
                    part3 = grid[i2:]   # bottom rectangle
                    a2 = self.minimumgridrea(part2)
                    a3 = self.minimumgridrea(part3)
                    res = min(res, a1 + a2 + a3)
            grid = self.rotate(grid)
        return res

    def minimumgridrea(self, grid: List[List[int]]) -> int:
        # Leetcode 3195
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

    def rotate(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        return [[grid[i][j] for i in range(n-1, -1, -1)] for j in range(m)]

if __name__ == "__main__":
    sol = Solution()
    grid = [[1,0,1],[1,1,1]]
    print(sol.minimumSum(grid))