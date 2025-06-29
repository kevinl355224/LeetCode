from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        """
        max(subsequences) + min(subsequences) <= target

        1 <= nums.length <= 10**5
        1 <= nums[i] <= 10**6
        """
        MOD = 10**9 + 7
        nums.sort()

        left = 0
        right = len(nums) - 1
        ans = 0

        # pow dict
        pow2 = [1] * len(nums)
        for i in range(1, len(nums)):
            pow2[i] = pow2[i - 1] * 2 % MOD

        while left <= right:
            if nums[left] + nums[right] <= target:
                ans = (ans + pow2[right - left]) % MOD
                left += 1
            else:
                right -= 1
        return ans

if __name__ == "__main__":
    sol = Solution()
    nums = [14,4,6,6,20,8,5,6,8,12,6,10,14,9,17,16,9,7,14,11,14,15,13,11,10,18,13,17,17,14,17,7,9,5,10,13,8,5,18,20,7,5,5,15,19,14]
    target = 22
    print(sol.numSubseq(nums, target))
