package main

import (
	"fmt"
	"math"
)

func dfs(nums []float64) bool {
	length := len(nums)
	if length == 1 {
		return math.Abs(nums[0]-24) < 1e-6
	}

	for i := 0; i < length; i++ {
		for j := i + 1; j < length; j++ {
			num1, num2 := nums[i], nums[j]
			nextNums := []float64{}
			for k := 0; k < length; k++ {
				if k != i && k != j {
					nextNums = append(nextNums, nums[k])
				}
			}
			for _, val := range []float64{num1 + num2, num1 - num2, num2 - num1, num1 * num2} {
				if dfs(append(nextNums, val)) {
					return true
				}
			}

			if math.Abs(num1) > 1e-6 && dfs(append(nextNums, num2/num1)) {
				return true
			}
			if math.Abs(num2) > 1e-6 && dfs(append(nextNums, num1/num2)) {
				return true
			}
		}
	}
	return false
}

func judgePoint24(cards []int) bool {
	floats := make([]float64, len(cards))
	for i, card := range cards {
		floats[i] = float64(card)
	}

	return dfs(floats)
}

func main() {
	cards := []int{4, 1, 8, 7}
	fmt.Println(judgePoint24(cards))
}
