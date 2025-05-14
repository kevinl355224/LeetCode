import numpy as np
from typing import List
from collections import Counter
from operator import itemgetter
from string import ascii_lowercase

'''
Use numpy will improve performance about 30%
'''

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        # s = "abcyy"
        # t = 2
        # num = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]

        # Could reference 3335/betterSol.py
        # Basic numpy int is int64, the biggest num is about 9.2e18
        # dtype=object could let numpy use basic python int which won't overflow
        count = np.array(itemgetter(*ascii_lowercase)(Counter(s)), dtype=object)
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
        matrix = np.array(matrix, dtype=object)

        def vec_mult(v, A):
            v = np.array(v, dtype=object)
            A = np.array(A, dtype=object)
            return [sum(v[k]*A[k][j] for k in range(26))%MOD
                    for j in range(26)] 
                    
        MOD = 10**9+7
        # Add Fast Exponentiation
        def fast_pow(vector, matrix, times):
            result = vector[:]
            base = matrix
            while times:
                if times & 1: # bitwise operation
                    result = np.dot(base, result) % MOD  
                    # result = np.dot(result, base) % MOD 
                base = np.dot(base, base) % MOD  
                times >>= 1
            return result
        
        ans = fast_pow(count, matrix, t)%MOD
        # print(ans)
        return sum(ans)%MOD


if __name__ == "__main__":
    sol = Solution()
    s = "abcyy"
    t = 2
    nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
    print(sol.lengthAfterTransformations(s=s, t=t, nums=nums))