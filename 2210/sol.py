from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        """
        Return the number of hills and valleys in nums.
        """
        ans = 0
        # if nums[1] > nums[0]:
        #     uphill = 1
        # elif nums[1] <  nums[0]:
        #     uphill = 0
        # else:
        #     uphill = None

        # for r in nums[2]

        # for i in range(2, len(nums) - 1):
        l = nums[0]
        m = nums[1]
        for r in nums[2:]:
            if r == m:
                continue
            if (m > l and m > r) or (m < l and m < r):
                ans += 1
            l = m
            m = r


        return ans
    
if __name__ == "__main__":
    sol = Solution()
    nums = [2,4,1,1,6,5]
    print(sol.countHillValley(nums))