import heapq
from typing import List

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        """
        binary
        1 = 0001
        2 = 0010
        3 = 0011
        
        1 ^(xor) 3 -> 0010
        a ^ k ^ K = a
        
        Pick 2 node in tree xor the same time is possible
        example:
            Tree : a -> b -> c -> d
            a^k, b^k -> b^k, c^k -> c^k, d^k  is equal to a^k, d^k, Xor the start and end.
        """
        # Xor all num in nums
        xor_diff = [0]*len(nums) # [-7, -6, -4, 1, 2.....] Negitive meaning the number is bigger after xor.
        total = sum(nums)
        
        for i, num in enumerate(nums):
            xor_diff[i] = (num ^ k) - num

        xor_diff.sort(reverse=True)

        for i in range(0, len(xor_diff)-1, 2):
            if xor_diff[i] + xor_diff[i+1] < 0:
                break
            total += xor_diff[i] + xor_diff[i+1]
        return total


if __name__ == "__main__":
    sol = Solution()

    nums = [54,31,15,86,7,19,53,91,14,37]
    k = 3
    edges = [[1,0],[1,2],[3,4],[5,7],[7,1],[8,3],[6,3],[1,6],[1,9]]
    print(sol.maximumValueSum(nums=nums, k=k, edges=edges))