from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        """
        Given an m x n binary matrix mat
        return the number of submatrices that have all ones.
        """
        # With Monotonic Stack
        rows, cols = len(mat), len(mat[0])
        ans = 0
        height = [0] * cols

        for r in range(rows):
            for c in range(cols):
                height[c] = height[c] + 1 if mat[r][c] == 1 else 0

            stack = []
            count = [0] * cols
            for c in range(cols):
                # If previous height is highter than current. Pop it.
                while stack and height[stack[-1]] >= height[c]:
                    stack.pop()
                
                # Current height is higher than before.
                if stack:
                    # prev_index is the height which is lower than current.
                    prev_index = stack[-1]
                    # count = the total count when prev_index + the height of current * (current - prev_idx)
                    count[c] = count[prev_index] + height[c] * (c - prev_index)
                # Current height is lower than before.
                else:
                    count[c] = height[c] * (c + 1)
                stack.append(c)
                ans += count[c]

        return ans



if __name__ == "__main__":
    sol = Solution()
    mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
    print(sol.numSubmat(mat))