from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        """
        Given an m x n binary matrix mat
        return the number of submatrices that have all ones.
        """
        rows, cols = len(mat), len(mat[0])
        ans = 0
        height = [0] * cols

        for r in range(rows):
            for c in range(cols):
                height[c] = height[c] + 1 if mat[r][c] == 1 else 0

            stack = []
            count = [0] * cols
            for i in range(cols):
                while stack and height[stack[-1]] >= height[i]:
                    stack.pop()
                if stack:
                    prev_index = stack[-1]
                    count[i] = count[prev_index] + height[i] * (i - prev_index)
                else:
                    count[i] = height[i] * (i + 1)
                stack.append(i)
                ans += count[i]

        return ans



if __name__ == "__main__":
    sol = Solution()
    mat = [[1,0,1],[1,1,0],[1,1,0]]
    print(sol.numSubmat(mat))