from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        1 <= numRows <= 30
        """
        pascal = [[1]]
        for row in range(1, numRows):
            new = [1] * (row + 1)
            # Calculate the half of the pascal.
            mid = (row // 2) + 1
            for i in range(1, mid):
                new[i] = new [row - i] = pascal[-1][i] + pascal[-1][i-1]

            pascal.append(new)
        return pascal
    
if __name__ == "__main__":
    sol = Solution()
    numRows = 5
    print(sol.generate(numRows))
