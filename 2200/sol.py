from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        """
        1 <= nums.length <= 1000
        """
        ans = []
        length = len(nums)
        right = 0
        for i in range(length):
            if nums[i] == key:
                left = max(i - k, right)
                right = min(i + k + 1, length)
                ans += range(left, right)
        return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [3,4,9,1,3,9,5]
    key = 9
    k = 1
    print(sol.findKDistantIndices(nums, key, k))

