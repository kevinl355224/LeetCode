from typing import List
from collections import deque

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        """
        Familiar with 3077 but fruits[i] and length both bigger. 

        Return the number of fruit types that remain unplaced after all possible allocations are made.

        n == fruits.length == baskets.length
        1 <= n <= 10**5
        1 <= fruits[i], baskets[i] <= 10**9
        """
        # Segment Tree
        length = len(baskets)
        seg = [0] * length * 4

        # build Segment Tree
        def build(node, l, r):
            if l == r:
                seg[node] = baskets[l]
                return 
            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            seg[node] = max(seg[node * 2], seg[node * 2 + 1])
        
        build(1, 0, length - 1)
        # print(seg)
        
        def find(node, l, r, fruit):
            if fruit > seg[node]: # If fruit is bigger than all seg
                return -1
            if l == r:
                seg[node] = -1 # baskets has been used
                return 1
            
            mid = (l + r) // 2
            candidate = find(node * 2, l, mid, fruit) # go left first
            if candidate == -1:
                candidate = find(node * 2 + 1, mid + 1, r, fruit) # if no candidate, go right
            seg[node] = max(seg[node * 2], seg[node * 2 + 1])
            return candidate
        
        res = 0
        for fruit in fruits:
            if find(1, 0, length - 1, fruit) == -1: res += 1
        return res


if __name__ == "__main__":
    sol = Solution()
    fruits = [4,2,5]
    baskets = [3,5,4,6,9,7]
    print(sol.numOfUnplacedFruits(fruits, baskets))