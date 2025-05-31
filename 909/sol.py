from collections import deque
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """
                        n
            [-1, -1, -1, -1, -1, -1]
            [-1, -1, -1, -1, -1, -1]
            [-1, -1, -1, -1, -1, -1]
        m   [-1, 35, -1, -1, 13, -1]
            [-1, -1, -1, -1, -1, -1]
            [-1, 15, -1, -1, -1, -1]
        Start from bottom left.
        Return the least number of dice rolls required to reach the square n2

        Try to find the fastest way to every cells
        """
        # for b in board:
        #     print(b)
        # Convert to line
        n = len(board)
        cells = [0]*((n**2)+1)
        reverse = 1
        idx = 1
        for y in board[::-1]:
            for x in y[::reverse]:
                cells[idx] = x
                idx += 1
            reverse *= -1

        # for idx, a in enumerate(cells):
        #     print(f"{idx}: {a}")

        visited = [False]*(n**2+1) # To record if the fastest way is found
        visited[1] = True
        dst = n**2
        # q = [step, cell]
        q = deque() 
        q.append((0, 1)) # start from 1 cell

        while q:
            step, cell = q.popleft()
            if cell == dst: 
                return step
            for idx in range(1,7):
                next = cell+idx
                if next > dst:
                    continue
                nextCell = next if cells[next] == -1 else cells[next]
                if not visited[nextCell]:
                    q.append([step+1, nextCell])
                    visited[nextCell] = True
        return -1

if __name__ == "__main__":
    board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
    sol = Solution()
    print(sol.snakesAndLadders(board))
