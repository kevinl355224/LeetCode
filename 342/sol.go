package main

import (
	"fmt"
)

func isPowerOfFour(n int) bool {
	if n <= 0 {
		return false
	}

	// count the 1 in binary
	binaryCnt := map[int]int{1: 0, 0: 0}
	for n > 0 {
		bit := n & 1
		binaryCnt[bit]++
		n >>= 1
	}
	fmt.Println(binaryCnt[1], binaryCnt[0])
	if binaryCnt[1] > 1 || binaryCnt[0]%2 == 1 {
		return false
	}
	return true
}

func main() {
	n := 16
	fmt.Println(isPowerOfFour(n))
}
