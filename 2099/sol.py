from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        """
        You want to find a subsequence of nums of length k that has the largest sum.
        Return any such subsequence as an integer array of length k.
        
        -10**5 <= nums[i] <= 10**5
        """
        nums_and_indices =  [(num, i) for i, num in enumerate(nums)]
        nums_and_indices.sort(key=lambda x:-x[0])
        top_k = sorted(nums_and_indices[:k], key=lambda x: x[1])
        return [num for num, i in top_k]

if __name__ == "__main__":
    sol = Solution()
    nums =  [-1,-2,3,4]
    k = 3
    print(sol.maxSubsequence(nums, k))
