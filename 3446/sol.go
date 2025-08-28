package main

import (
	"fmt"
	"sort"
)

func sortMatrix(grid [][]int) [][]int {
	n := len(grid)

	for i := range n {
		temp := make([]int, n-i)
		for j := range n - i {
			temp[j] = grid[i+j][j]
		}
		sort.Sort(sort.Reverse(sort.IntSlice(temp)))
		for j := range n - i {
			grid[i+j][j] = temp[j]
		}
	}

	for j := 1; j < n; j++ {
		temp := make([]int, n-j)
		for i := range n - j {
			temp[i] = grid[i][i+j]
		}
		sort.Ints(temp)

		for i := range n - j {
			grid[i][j+i] = temp[i]
		}
	}

	return grid
}

func main() {
	grid := [][]int{{1, 7, 3}, {9, 8, 2}, {4, 5, 6}}
	fmt.Println(sortMatrix(grid))
}
