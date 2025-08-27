from typing import List
from functools import lru_cache

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        directions = [(1, -1), (1, 1), (-1, 1), (-1, -1)] # x, y of top-right, down-right, down-left, top-left
        cols = len(grid[0])
        rows = len(grid)
        max_len = 0

        # Find longest path for dp[i][j]
        @lru_cache(None)
        def dfs(x, y, dir, expected, rotate:bool):
            if x < 0 or x >= cols or y < 0 or y >= rows:
                return 0

            if grid[y][x] == expected:
                # Try same dir
                new_x = x + directions[dir][0]
                new_y = y + directions[dir][1]
                
                nxt = 2 if expected == 0 else 0

                length = dfs(new_x, new_y, dir, nxt, rotate) + 1

                # Try rotate clockwise
                if not rotate:
                    new_dir = (dir + 1) % 4
                    new_x = x + directions[new_dir][0]
                    new_y = y + directions[new_dir][1]
                    rotate_lenght = dfs(new_x, new_y, new_dir, nxt, True) + 1
            
                    return max(length, rotate_lenght)
                return length
                
            else:
                return 0
            
        # Find 1
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    # Try four dir
                    for i in range(4):
                        length = 1 + dfs(col + directions[i][0], row + directions[i][1], i, 2, False)
                        max_len = max(max_len, length)

        return max_len

if __name__ == "__main__":
    sol = Solution()
    grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
    print(sol.lenOfVDiagonal(grid))