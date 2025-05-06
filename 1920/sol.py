from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # [0,2,1,5,3,4] <- index
        # ---->
        return [nums[nums[i]] for i in range(len(nums))] #List Comprehension will faster than for loop.

if __name__ == "__main__":
    sol = Solution()
    print(sol.buildArray(nums = [0,2,1,5,3,4]))