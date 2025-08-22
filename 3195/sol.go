package main

import (
	"fmt"
	"math"
)

func checkEdge(edge *[]int, point int) {
	if (*edge)[0] > point {
		(*edge)[0] = point
	}

	if (*edge)[1] < point {
		(*edge)[1] = point
	}
}

func minimumArea(grid [][]int) int {
	// 1 <= grid.length, grid[i].length <= 1000
	width := []int{math.MaxInt32, -1}
	height := []int{math.MaxInt32, -1}

	for row := range grid {
		for col := range grid[row] {
			if grid[row][col] == 1 {
				checkEdge(&width, col)
				checkEdge(&height, row)
			}
		}
	}

	return (width[1] - width[0] + 1) * (height[1] - height[0] + 1)
}

func main() {
	grid := [][]int{{0, 1, 0}, {1, 0, 1}}
	fmt.Println(minimumArea(grid))
}
