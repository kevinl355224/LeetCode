from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        k = maximum value of the bitwise AND of any subarray of nums.
        Return the length of the longest such subarray with a bitwise AND equal to k.

        1 <= nums.length <= 10**5
        1 <= nums[i] <= 10**6
        """

        max_cnt = cnt = 0
        max_num = max(nums)
        for num in nums:
            if num == max_num:
                cnt += 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 0
        max_cnt = max(max_cnt, cnt) 
        return max_cnt

if __name__ == "__main__":
    sol = Solution()
    nums = [3,3,3,3,1,2,3,3,2,2,3]
    print(sol.longestSubarray(nums))