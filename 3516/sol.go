package main

import "fmt"

func getDistance(a int, b int) int {
	if a >= b {
		return a - b
	} else {
		return b - a
	}
}

func findClosest(x int, y int, z int) int {
	diff := getDistance(x, z) - getDistance(y, z)
	switch {
	case diff < 0:
		return 1
	case diff > 0:
		return 2
	default:
		return 0
	}
}

func main() {
	x, y, z := 2, 7, 4
	fmt.Println(findClosest(x, y, z))
}
