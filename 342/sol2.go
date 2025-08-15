package main

import (
	"fmt"
)

func isPowerOfFour(n int) bool {
	if n <= 0 {
		return false
	}

	// Check if n has only one '1' bit in its binary representation.
	// n = 1000, n - 1  = 0111.
	if n&(n-1) != 0 {
		return false
	}
	// 0x55 = 01010101  Used to check if the single '1' bit is in an even position
	return n&0x55555555 != 0
}

func main() {
	n := 16
	fmt.Println(isPowerOfFour(n))
}
