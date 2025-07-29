from typing import List
from collections import defaultdict

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        """
        Return an integer array answer of size n where answer[i] is the length of the minimum sized subarray starting at i with maximum bitwise OR.

        1 <= n <= 10**5
        0 <= nums[i] <= 10**9
        """
        length = len(nums)
        result = [float("inf")] * length

        for i in range(length):
            result[i] = 1
            j = i - 1
            while j >= 0 and nums[j] | nums[i] != nums[j]:
                result[j] = i - j + 1
                # Convert nums[j] into max_or
                nums[j] |= nums[i]
                j -= 1

        return result

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,2,3,4,6,1,1,7,7]
    print(sol.smallestSubarrays(nums))