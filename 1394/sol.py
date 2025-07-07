from typing import List
from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        """
        Given an array of integers arr, 
        a lucky integer is an integer that has a frequency in the array equal to its value.

        Return the largest lucky integer in the array. 
        If there is no lucky integer return -1.

        1 <= arr.length <= 500
        1 <= arr[i] <= 500
        """
        cnt = Counter(arr)
        max_lucky = -1
        for k, v in cnt.items():
            if k == v:
                max_lucky = max(max_lucky, k)
        return max_lucky

if __name__ == "__main__":
    sol = Solution()
    arr = [2,2,3,4]
    print(sol.findLucky(arr))
