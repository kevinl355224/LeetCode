from typing import List

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        # nums1 = [3,2,0,1,0]
        # nums2 = [6,5,0]
        sum1, sum2 = sum(nums1), sum(nums2)
        nums1Zero = nums1.count(0)
        nums2Zero = nums2.count(0)
        # Swap num's 0 to 1
        swap1 = sum1 + nums1Zero
        swap2 = sum2 + nums2Zero

        # If swap2 is bigger than swap1, but nums1 don't have any 0 to swap to bigger number. Then fail.
        if (nums1Zero == 0 and swap2 > swap1) or (nums2Zero == 0 and swap1 > swap2):
            return -1
        return max(swap1, swap2)

if __name__ == "__main__":
    nums1 = [3,2,0,1,0]
    nums2 = [6,5,0]
    sol = Solution()
    print(sol.minSum(nums1, nums2))
