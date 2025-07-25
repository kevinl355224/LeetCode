from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        """
        Delete any number of elements from nums without making it empty.
        All elements in the subarray are unique.
        The sum of the elements in the subarray is maximized.

        1 <= nums.length <= 100
        -100 <= nums[i] <= 100
        """

        return sum([x for x in set(nums) if x > 0]) if max(nums) > 0 else max(nums)

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4,5]
    print(sol.maxSum(nums))