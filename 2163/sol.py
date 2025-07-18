from heapq import heapify, heapreplace
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        """
        nums consisting of 3 * n elements.
        Remove any subsequence of elements of size exactly n from nums

        sum_first = new_nums[:n]
        sum_second = new_nums[n:]

        Return the minimum difference possible between the sums of the two parts after the removal of n elements.

        nums.length == 3 * n
        1 <= n <= 10**5
        1 <= nums[i] <= 10**5
        """
        # Have to let sum_second > sum_first. Let the second half bigger than first half.
        n = len(nums) // 3

        """
        [7,9,5,8,1,3]
         * *          Must be first half
             * *      Could be first or second half
                 * *  Must be second half
        """
        # Init
        diff = [0] * (n + 1)
        # left_half should keep small. Have to remove bigger number first
        heapify(left_half := [-num for num in nums[:n]])
        heapify(right_half := nums[2*n:])

        # Process first half
        total = sum(nums[:n])
        min_diff = total
        for i in range(n, 2 * n + 1):
            diff[i - n] = total
            if nums[i] >= -left_half[0]:
                continue
            # left half is negtive
            total += nums[i] + left_half[0]
            heapreplace(left_half, -nums[i])

        # Process second half (From rigth to left)
        total = sum(nums[2*n:])
        min_diff -= total
        for i in range(2*n-1, n-2, -1):
            diff[i-n+1] -= total
            min_diff = min(min_diff, diff[i-n+1])
            if nums[i] <= right_half[0]:
                continue
            total += nums[i] - right_half[0]
            heapreplace(right_half, nums[i])
        return min_diff
    

if __name__ == "__main__":
    sol = Solution()
    nums = [47, 26, 21, 40, 3, 20, 12, 19, 1, 11, 37, 49, 50, 29, 23, 32, 27, 10, 49, 24, 44, 43, 46, 27, 2, 3, 41, 35, 10, 49, 38, 44, 6, 27, 27, 43, 5, 36, 37, 16, 5, 30, 12, 15, 6, 50, 44, 40, 17, 45, 24, 33, 32, 4, 35, 37, 15, 17, 13, 21]
    print(sol.minimumDifference(nums))