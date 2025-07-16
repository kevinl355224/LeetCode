from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        """
        (sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.

        2 <= nums.length <= 2 * 10**5
        1 <= nums[i] <= 10**7
        A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
        
        Return the length of the longest valid subsequence of nums.
        """
        odd_cnt = 0
        convert_lenght = 0
        pre = None

        for i in range(len(nums)):
            is_odd = nums[i] & 1
            if is_odd:
                odd_cnt += 1
            if pre != is_odd:
                convert_lenght += 1
            pre = is_odd

        return max(len(nums) - odd_cnt, odd_cnt, convert_lenght)

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,1,1,2,1,2]
    print(sol.maximumLength(nums))