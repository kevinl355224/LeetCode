import numpy as np
from typing import List
from collections import Counter
from operator import itemgetter
from string import ascii_lowercase


import numpy as np
class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        # s = "abcyy"
        # t = 2
        # num = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]

        # Could reference 3335/betterSol.py
        count = np.array(itemgetter(*ascii_lowercase)(Counter(s)))
        # count = [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0]

        # Count matrix
        matrix = [[0 for _ in range(26)] for _ in range(26)]
        # Each word a-z
        for i in range(26):
            vector = []
            for j in range(26):
                if i != j and nums[j] >= (i-j+26)%26:
                    # print(f"i: {i}, j: {j}, nums[i]: {nums[i]}, (i-j+26)%26: {(i-j+26)%26}" )
                    matrix[i][j]=1

        # Matrix is 2D
        # Count is 1D
        matrix = np.array(matrix)
        # new_count = np.dot(matrix, count)
        MOD = 10**9+7
        for _ in range(t):
            count = np.dot(matrix, count)%MOD
        
        # print(sum(count)%(10**9+7))
        # return sum(count)%(10**9+7)
        return sum(count)%MOD


if __name__ == "__main__":
    sol = Solution()
    s = "abcyy"
    t = 2
    # nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
    nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
    print(sol.lengthAfterTransformations(s=s, t=t, nums=nums))