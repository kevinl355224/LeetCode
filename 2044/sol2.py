from typing import List
from collections import Counter
from functools import reduce

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        prevBits = Counter([0])
        for num in nums:
            for prev, count in list(prevBits.items()):
                prevBits[prev | num] += count
        max_or = reduce(lambda a,b: a|b, nums)
        return prevBits[max_or]
    
if __name__ == "__main__":
    sol = Solution()
    nums = [3,1,2]
    print(sol.countMaxOrSubsets(nums))