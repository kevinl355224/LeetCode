package main

import "fmt"

func findDiagonalOrder(mat [][]int) []int {
	direction := 1
	x, y := 0, 0
	m, n := len(mat), len(mat[0])
	result := []int{}

	var new_x, new_y int

	for range n * m {
		result = append(result, mat[y][x])
		if direction == 1 {
			new_x = x + 1
			new_y = y - 1
		} else {
			new_x = x - 1
			new_y = y + 1
		}

		if new_x < 0 || new_x >= n || new_y < 0 || new_y >= m {
			if direction == 1 {
				if x+1 < n {
					x += 1
				} else {
					y += 1
				}
			} else {
				if y+1 < m {
					y += 1
				} else {
					x += 1
				}
			}
			direction ^= 1
		} else {
			x, y = new_x, new_y
		}
	}

	return result
}

func main() {
	mat := [][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
	fmt.Println(findDiagonalOrder(mat))

}
