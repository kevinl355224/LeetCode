from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        coordinates = []
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    coordinates.append((i,j))
                else:
                    val = board[i][j]
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[(i // 3) * 3 + (j // 3)].add(val)

        def solve(it: int) -> bool:
            if it == len(coordinates):
                return True
            i = coordinates[it][0]
            j = coordinates[it][1]
            b = (i // 3) * 3 + (j // 3)
            for num in '123456789':
                if num not in rows[i] and num not in cols[j] and num not in boxes[b]:
                    board[i][j] = num
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[b].add(num)
                    if solve(it + 1):
                        return True
                    board[i][j] = '.'
                    rows[i].remove(num)
                    cols[j].remove(num)
                    boxes[b].remove(num)
            return False

        solve(0)


if __name__ == "__main__":
    sol = Solution()
    board = \
        [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2","8",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    sol.solveSudoku(board)