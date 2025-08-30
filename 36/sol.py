from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[int]]) -> int:
        """
        board.length == 9
        board[i].length == 9
        """
        cols, rows = len(board[0]), len(board)
        
        for col in range(cols):
            temp = []
            for row in range(rows):
                if board[row][col].isdigit():
                    if board[row][col] in temp:
                        return False
                    temp.append(board[row][col])

        for row in range(rows):
            temp = []
            for col in range(cols):
                if board[row][col].isdigit():
                    if board[row][col] in temp:
                        return False
                    temp.append(board[row][col])


        for x in range(3):
            for y in range(3):
                temp = []
                for row in range(3):
                    for col in range(3):
                        num = board[3*y + row][3*x + col]
                        if num.isdigit():
                            if num in temp:
                                return False
                            temp.append(num)
        return True
    
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
    print(sol.isValidSudoku(board))