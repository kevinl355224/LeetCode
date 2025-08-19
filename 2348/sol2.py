from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        """
        Return the number of subarrays filled with 0.
        """
        zeors = cnt = 0
        for num in nums:
            if num == 0:
                zeors += 1
                cnt += zeors
            else:
                zeors = 0
        return cnt



if __name__ == "__main__":
    sol = Solution()
    nums = [1,3,0,0,2,0,0,4]
    print(sol.zeroFilledSubarray(nums))