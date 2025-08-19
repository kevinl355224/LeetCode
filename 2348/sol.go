package main

import "fmt"

func zeroFilledSubarray(nums []int) int64 {
	cnt, zeros := 0, 0
	for _, num := range nums {
		if num == 0 {
			zeros += 1
			cnt += zeros
		} else {
			zeros = 0
		}
	}
	return int64(cnt)
}

func main() {
	nums := []int{1, 3, 0, 0, 2, 0, 0, 4}
	fmt.Println(zeroFilledSubarray(nums))
}
