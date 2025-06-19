from typing import List

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        """
        partition nums into one or more subsequences 
        such that each element in nums appears in exactly one of the subsequences.
        
        Return the minimum number of subsequences needed 
        such that the difference between the maximum and minimum values in each subsequence is at most k.
        """
        nums.sort()
        cnt = 1
        min_num = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - min_num > k:
                cnt += 1
                min_num = nums[i]
        
        return cnt

if __name__ == "__main__":
    sol = Solution()
    nums = [3,6,1,2,5]
    k = 2
    print(sol.partitionArray(nums, k))