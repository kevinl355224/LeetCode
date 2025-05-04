from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        for val in range(1, 7):
            # Initialize
            top_swap = bottom_swap = 0
            valid = False
            for top ,bottom in zip(tops, bottoms):
                if top != val and bottom != val:
                    # This num is't conform.
                    valid = False
                    break
                if top != val:
                    top_swap += 1
                if bottom != val:
                    bottom_swap += 1
                valid = True
            if valid:
                return min(top_swap, bottom_swap)        
        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.minDominoRotations(tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]))