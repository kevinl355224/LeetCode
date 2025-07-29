from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        last = [0] * 32

        for i in range(n - 1, -1, -1):
            for bit in range(32):
                if nums[i] & (1 << bit):
                    last[bit] = i  # The last bit is appear when i
            # max_j = i
            # for bit in range(32):
            #     if last[bit] > max_j:
            #         max_j = last[bit]
            # result[i] = max_j - i + 1
            result[i] = max(max(last), i) - i + 1
        return result
    
if __name__ == "__main__":
    sol = Solution()
    nums = [1,0]
    print(sol.smallestSubarrays(nums))