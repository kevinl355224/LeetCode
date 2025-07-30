from typing import List
from itertools import groupby

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_n = max(nums)
        return max(len(list(it)) for n, it in groupby(nums) if n == max_n)
    
if __name__ == "__main__":
    sol = Solution()
    nums = [3,3,3,3,1,2,3,3,2,2,3]
    print(sol.longestSubarray(nums))