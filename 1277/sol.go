package main

import "fmt"

func countSquares(matrix [][]int) int {
	cnt := 0
	rows, cols := len(matrix), len(matrix[0])
	dp := make([][]int, rows)
	for i := range matrix {
		dp[i] = make([]int, cols)
	}

	for i := range rows {
		for j := range cols {
			if matrix[i][j] == 1 {
				if i == 0 || j == 0 {
					dp[i][j] = 1
				} else {
					dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
				}

				cnt += dp[i][j]
			}
		}
	}
	return cnt

}

func main() {
	matrix := [][]int{{0, 1, 1, 1}, {1, 1, 1, 1}, {0, 1, 1, 1}}
	fmt.Println(countSquares(matrix))
}
