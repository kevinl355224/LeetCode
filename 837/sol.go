package main

import "fmt"

func new21Game(n int, k int, maxPts int) float64 {
	dp := make([]float64, n+1)
	dp[0] = 1
	window_sum := 1.0
	ans := 0.0

	if k == 0 || n >= k+maxPts {
		return 1.0
	}

	for i := 1; i < n+1; i++ {
		dp[i] = window_sum / float64(maxPts)

		if i < k {
			window_sum += dp[i]
		} else {
			ans += dp[i]
		}
		if i-maxPts >= 0 {
			window_sum -= dp[i-maxPts]
		}
	}
	return ans
}

func main() {
	n := 21
	k := 17
	maxPts := 10
	fmt.Println(new21Game(n, k, maxPts))
}
