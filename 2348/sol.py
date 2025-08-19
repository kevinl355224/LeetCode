from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        """
        Return the number of subarrays filled with 0.
        """
        # Use two pointer
        left = -1
        right = cnt = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                right = i
                cnt += right -left
            else:
                left = i
        return cnt



if __name__ == "__main__":
    sol = Solution()
    nums = [1,3,0,0,2,0,0,4]
    print(sol.zeroFilledSubarray(nums))