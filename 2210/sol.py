from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        """
        Return the number of hills and valleys in nums.
        """
        ans = 0
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