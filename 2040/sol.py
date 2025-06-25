import math
from typing import List
from bisect import bisect_right, bisect_left

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """
        1 <= nums1.length, nums2.length <= 5 * 10**4
        nums1 = [-4,-2,0,3]
        nums2 = [2,4]

        Return the kth (1-based) smallest product of nums1[i] * nums2[j]
        """

        def count_products(x):
            # Count all product that smaller than x.
            cnt = 0
            for a in nums1:
                if a > 0:
                    """
                    "bisect_right"
                    nums2 = [2,4,4,6] 
                    If x//a=4, return 3
                    """
                    cnt += bisect_right(nums2, x // a) # biggest b == x // a
                elif a < 0:
                    cnt += len(nums2) - bisect_left(nums2, math.ceil(x / a))
                else:
                    #　ａ == 0
                    if x >= 0:
                        cnt += len(nums2)
            return cnt

        # Binary search for the product (nums1 * nums2)
        # -10**5 <= nums1[i], nums2[j] <= 10**5
        left = -10 ** 10
        right = 10 ** 10

        while left < right:
            mid = (left + right) // 2
            if count_products(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left

if __name__ == "__main__":
    sol = Solution()
    nums1 = [-4, -2, 0, 3]
    nums2 = [-1, 2, 4]
    k = 6
    print(sol.kthSmallestProduct(nums1, nums2, k))