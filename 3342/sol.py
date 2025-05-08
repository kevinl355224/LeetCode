import heapq
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # [[0,4,5],[4,4,5],[5,5,5]]
        #               m(x)
        #   start -> 0  4  5
        #       n(y) 4  4  5 
        #            5  5  5 <- goal
        # 1s 1st move, 2s sec move, 1s 3rd move .etc
        # Use a array[n*m] records the minimum time to reach.

        heap = [(0,0,0,0)] # [(times, step, y, x),..]
        n = len(moveTime)
        m = len(moveTime[0])

        directions = [(0,1), (0,-1), (-1,0), (1,0)] # right, left, up, down

        # Adding a function call slows down the performance by about 100ms.
        def notInBorder(y, x):
            return not(0 <= y < n and 0 <= x < m and moveTime[y][x] != -1)
        
        moveTime[0][0] = -1
        while heap:
            times, step, y, x = heapq.heappop(heap)  
            # Reach end
            if (y, x) == (n-1, m-1):
                return times
            
            for dy, dx in directions:
                ny, nx = y+dy, x+dx
                # If reach the border then skip.
                if notInBorder(ny, nx):
                    continue
                nextStep = 2 if step%2 else 1
                nextTime = max(times, moveTime[ny][nx]) + nextStep

                moveTime[ny][nx] = -1
                heapq.heappush(heap, (nextTime, nextStep, ny, nx))

if __name__ == "__main__":
    sol = Solution()
    test = [[0,4,5],[4,4,5],[5,5,5]]
    print(sol.minTimeToReach(moveTime=test))