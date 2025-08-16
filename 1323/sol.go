package main

import (
	"fmt"
	"math"
)

func maximum69Number(num int) int {
	// 1 <= num <= 10**4
	numStr := fmt.Sprint(num)
	length := len(numStr)
	for i, digit := range numStr {
		fmt.Println(i, digit)
		if digit == 54 {
			return num + 3*int(math.Pow(10, float64(length-i-1)))
		}
	}
	return num
}

func main() {
	num := 696
	fmt.Println(maximum69Number(num))
}
