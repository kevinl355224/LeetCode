from typing import List

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        """
        Given a circular array nums, find the maximum absolute difference between adjacent elements.

        2 <= nums.length <= 100
        """
        max_diff = -float("inf")
        for i in range(len(nums)):
            max_diff = max(abs(nums[i] - nums[i -1]), max_diff)
        return max_diff
    
if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,4]
    print(sol.maxAdjacentDistance(nums))