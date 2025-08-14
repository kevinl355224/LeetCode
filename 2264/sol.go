package main

import (
	"fmt"
)

func largestGoodInteger(num string) string {
	cnt := 1
	var max byte = 0

	for i := 1; i < len(num); i++ {
		if num[i] == num[i-1] {
			cnt++
		} else {
			cnt = 1
		}
	
		if cnt >= 3 && num[i] > max {
			max = num[i]
			if max == '9' {
				break
			}
		}
	}

	if max == 0 {
		return ""
	}

	return string([]byte{max, max, max})
}


func main() {

	num := "077133399"
	fmt.Println(largestGoodInteger(num))
	
}