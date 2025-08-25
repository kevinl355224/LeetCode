from typing import List
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
        return an array of all the elements of the array in a diagonal order.

        1 <= m, n <= 10**4
        1 <= m * n <= 10**4
        -10**5 <= mat[i][j] <= 10**5
        """
        # Init
        direction = 1 # 1 = UpRight, -1 = DownLeft
        x, y = 0, 0 # start with x = 0, y = 0
        m, n = len(mat), len(mat[0])
        result = []
        # Start
        for _ in range(n * m):
            result.append(mat[y][x])

            # Move
            new_x = x + (1 if direction == 1 else -1)
            new_y = y + (-1 if direction == 1 else 1)

            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
                if direction == 1:
                    if x + 1 < n:
                        x += 1
                    else:
                        y += 1
                else:
                    if y + 1 < m:
                        y += 1
                    else:
                        x += 1
                direction ^= 1
            else:
                x, y = new_x, new_y

        return result

if __name__ == "__main__":
    sol = Solution()
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    print(sol.findDiagonalOrder(mat))