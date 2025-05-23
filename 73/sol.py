from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        m = len(matrix)
        x_0_idx = set()
        y_0_idx = set()
        # locate the 0 in matrix
        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                if num == 0:
                    x_0_idx.add(j)
                    y_0_idx.add(i)

        for y in y_0_idx:
            for j in range(n): 
                matrix[y][j] = 0

        for x in x_0_idx:
            for i in range(m):
                matrix[i][x] = 0

        print_matix(matrix)

if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    sol.setZeroes(matrix)
