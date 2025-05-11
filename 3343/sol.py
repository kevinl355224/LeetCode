from functools import lru_cache 
from math import comb

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10**9 + 7  # Modulo for large numbers
        digit_count = [0] * 10  # Count of each digit (0–9)

        # Count frequency of each digit in the input string
        for digit in num:
            digit_count[int(digit)] += 1

        total_digits = len(num)  # Total number of digits
        total_sum = sum(int(digit) for digit in num)  # Sum of all digits

        # If the total sum is odd, it cannot be split evenly
        if total_sum % 2:
            return 0

        left_sum = [0] * 10  # left_sum[i] = sum of digits from i to 9
        left_count = [0] * 10  # left_count[i] = total digits from i to 9
        result_cache = [1] * 11  # Stores factorial combinations for reuse

        current_sum = 0  # Running sum from digits i to 9
        current_count = 0  # Running count of digits from i to 9
        for i in range(9, -1, -1):
            print(result_cache)
            current_sum += i * digit_count[i]
            current_count += digit_count[i]
            left_sum[i] = current_sum
            left_count[i] = current_count
            result_cache[i] = result_cache[i + 1] * comb(left_count[i], digit_count[i]) % MOD

        # DFS with memoization to explore digit distribution
        @lru_cache(None)
        def dfs(i, remaining_sum, remaining_count):
            # If both sum and count match exactly, return permutations for remaining digits
            if remaining_sum == 0 and remaining_count == 0:
                return result_cache[i]

            # If we’ve run out of digits or exceeded limits, return 0
            if i == 10 or remaining_sum > left_sum[i] or remaining_count > left_count[i]:
                return 0

            result = 0
            target_sum = remaining_sum

            # Try distributing digit `i`: choose `x` digits for even, remaining for odd
            for x in range(digit_count[i] + 1):
                y = digit_count[i] - x
                # target_sum is not enough.
                # Don't have enough digit to even or odd. 
                if target_sum < 0 or remaining_count < x or y > left_count[i] - remaining_count:
                    target_sum -= i
                    continue

                temp_result = dfs(i + 1, target_sum, remaining_count - x) * comb(remaining_count, x) % MOD
                result = (result + temp_result * comb(left_count[i] - remaining_count, y)) % MOD
                target_sum -= i
            return result

        # Start DFS to distribute digits such that both parts are balanced
        # total_sum // 2, total_digits//2 is the "even" target_sum and target_digits have to reach
        # Ex. 96421 target_sum = 11 target_digits = 2
        # once put 2 and 9 into event position, remaining_sum = remaining_digit =0, return result_cache[i]
        return dfs(0, total_sum // 2, total_digits // 2)

if __name__ == "__main__":
    sol = Solution()
    test = "96421"
    print(sol.countBalancedPermutations(num=test))