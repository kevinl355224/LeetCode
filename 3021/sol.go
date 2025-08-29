package main

import "fmt"

func flowerGame(n int, m int) int64 {
	return int64(((n+1)/2)*(m/2) + (n/2)*((m+1)/2))
}

func main() {
	n, m := 2, 3

	fmt.Println(flowerGame(n, m))
}
