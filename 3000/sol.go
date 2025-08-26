package main

import "fmt"

func areaOfMaxDiagonal(dimensions [][]int) int {
	maxArea, maxDiag := 0, 0

	for _, rect := range dimensions {
		w, l := rect[0], rect[1]
		newDiag := w*w + l*l
		if newDiag > maxDiag {
			maxDiag = newDiag
			maxArea = w * l
		} else if newDiag == maxDiag {
			maxArea = max(maxArea, w*l)
		}
	}
	return maxArea
}

func main() {
	dimensions := [][]int{{9, 3}, {8, 6}}
	fmt.Println((areaOfMaxDiagonal(dimensions)))
}
