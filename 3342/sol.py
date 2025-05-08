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

        heap = [] # [(times, step, y, x),..]
        n = len(moveTime)
        m = len(moveTime[0])
        minTime = [[float('inf')]*m for _ in range(n)]

        directions = [(0,1), (0,-1), (-1,0), (1,0)] # right, left, up, down

        heapq.heappush(heap, (0,0,0,0))

        def notInBorder(y, x):
            return not(0 <= ny < n and 0 <= nx < m)

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
                if nextTime < minTime[ny][nx]:
                    minTime[ny][nx] = nextTime
                    heapq.heappush(heap, (nextTime, nextStep, ny, nx))

if __name__ == "__main__":
    sol = Solution()
    test = [[0,4,5],[4,4,5],[5,5,5]]
    print(sol.minTimeToReach(moveTime=test))