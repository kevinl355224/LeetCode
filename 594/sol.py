from typing import List
from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        """
        max(subsequences) - min(subsequences) = 1
        return the length of its longest subsequences

        1 <= nums.length <= 2 * 10**4
        -10**9 <= nums[i] <= 10**9
        """
        max_length = 0

        cnt = Counter(nums)

        # print(ordered_tuple)
        for num in cnt:
            if num + 1 in cnt:
                max_length = max(max_length, cnt[num] + cnt[num + 1])

        return max_length

if __name__ == "__main__":
    sol = Solution()
    nums = [1,3,2,2,5,2,3,7]
    print(sol.findLHS(nums))