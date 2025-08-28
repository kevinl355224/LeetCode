from typing import List

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        """
        n * n Square
        The diagonals in the bottom-left triangle (including the middle diagonal) are sorted in decreasing order.
        The diagonals in the top-right triangle are sorted in accending order.

        1 <= n <= 10
        -10 ** 5 <= grid[i][j] <= 10**5
        """
        n = len(grid)

        # Process bottom-left
        for i in range(n):
            temp = [grid[i + j][j] for j in range(n - i)]
            temp.sort(reverse=True)
            print(temp)
            for j in range(n-i):
                grid[i + j][j] = temp[j]

        # Process top-right
        for j in range(1, n):
            tmp = [grid[i][j + i] for i in range(n - j)]
            tmp.sort()
            for i in range(n - j):
                grid[i][j + i] = tmp[i]

        return grid

if __name__ == "__main__":
    sol = Solution()
    grid = [[1,7,3],[9,8,2],[4,5,6]]
    print(sol.sortMatrix(grid))