package main

import "fmt"

func numSubmat(mat [][]int) int {
	// Monotonic Stack
	rows, cols := len(mat), len(mat[0])
	ans := 0
	height := make([]int, cols)

	for r := range rows {
		for c := range cols {
			if mat[r][c] == 1 {
				height[c]++
			} else {
				height[c] = 0
			}
		}

		stack := []int{}
		count := make([]int, cols)
		for c := range cols {
			// pop all higher stick before.
			for len(stack) > 0 && height[stack[len(stack)-1]] > height[c] {
				stack = stack[:len(stack)-1] // pop
			}

			if len(stack) > 0 {
				prev_index := stack[len(stack)-1]
				count[c] = count[prev_index] + height[c]*(c-prev_index)
			} else {
				count[c] = height[c] * (c + 1)
			}

			stack = append(stack, c)
			ans += count[c]
		}
	}
	return ans
}

func main() {
	mat := [][]int{{0, 1, 1, 0}, {0, 1, 1, 1}, {1, 1, 1, 0}}
	fmt.Println(numSubmat(mat))

}
