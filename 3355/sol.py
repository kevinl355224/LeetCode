from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        """
        Use difference array
        """
        diff = [0]*(len(nums)+1)
    
        for l, r in queries:
            diff[l] += 1
            diff[r+1] -= 1 
        
        rsum = 0
        # Check nums
        for i in range(len(nums)):
            rsum += diff[i]
            if nums[i] > rsum:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    nums = [1,0,1]
    queries = [[0,2]]
    print(sol.isZeroArray(nums, queries))