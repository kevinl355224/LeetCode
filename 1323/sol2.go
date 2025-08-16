package main

import (
	"fmt"
	"strconv"
	"strings"
)

func maximum69Number(num int) int {
	// 1 <= num <= 10**4
	s := strconv.Itoa(num)
	s = strings.Replace(s, "6", "9", 1)
	ans, _ := strconv.Atoi(s)
	return ans
}

func main() {
	num := 696
	fmt.Println(maximum69Number(num))
}
