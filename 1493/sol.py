from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        "Must"  delete one element from list.
        Return the size of the longest non-empty subarray containing only 1
        Return 0 if there is no such subarray.

        1 <= nums.length <= 10**5
        """
        if 1 not in nums :
            return 0

        if nums.count(0) <= 1 :
            return len(nums) - 1

        # sliding window
        left = zeros = max_lenght = 0

        for right, num in enumerate(nums):
            if num == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            max_lenght = max(max_lenght, right - left)
                
        return max_lenght

if __name__ == "__main__":
    sol = Solution()
    nums = [1,0,0,0,0]
    print(sol.longestSubarray(nums))