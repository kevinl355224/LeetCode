from typing import List
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        """
        (sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k.

        2 <= nums.length <= 10**3
        1 <= nums[i] <= 10**7
        1 <= k <= 10**3

        A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
        
        Return the length of the longest valid subsequence of nums.
        """
        n = len(nums)
        dp = [[1] * k for _ in range(n)]
        max_length = 1
        # Calculate length of subsquence end with nums[i]
        for i in range(len(nums)):
            for j in range(i):
                mod = (nums[i] + nums[j]) % k
                # If index j is from small to big, bigger j must has bigger length with specific mod. 
                dp[i][mod] = dp[j][mod] + 1
                max_length = max(max_length, dp[i][mod])

        return max_length

if __name__ == "__main__":
    sol = Solution()
    nums = [1,4,2,3,1,4]
    k = 3
    print(sol.maximumLength(nums, k))