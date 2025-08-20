func countSquares(matrix [][]int) int {

	sum := 0

	for r := 0; r < len(matrix); r++ {
		for c := 0; c < len(matrix[r]); c++ {
			if matrix[r][c] == 0 {
				continue
			}
			if r > 0 && c > 0 {
				matrix[r][c] = 1 + min(matrix[r][c-1], matrix[r-1][c-1], matrix[r-1][c])
			}
			sum += matrix[r][c]
		}
	}

	return sum

}