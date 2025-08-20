from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        """
        Given a m * n matrix of ones and zeros
        return how many square submatrices have all ones

        1 <= arr.length, arr[0].length <= 300
        """
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        cnt = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    # Safe to access neighbors (no boundary problem)
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
                    cnt += dp[i][j]
        return cnt



if __name__ == "__main__":
    sol = Solution()
    matrix =[
            [0,1,1,1],
            [1,1,1,1],
            [0,1,1,1]
            ]
    print(sol.countSquares(matrix))