import heapq
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # [[0,4,5],[4,4,5],[5,5,5]]
        #               m(x)
        #   start -> 0  4  5
        #       n(y) 4  4  5 
        #            5  5  5 <- goal
        # 1 sec / move
        # Use a array[n*m] records the minimum time to reach.
        n = len(moveTime)
        m = len(moveTime[0])
        minTime = [[float('inf')]*m for _ in range(n)]
        heap = []
        directions = [(0,1), (0,-1), (1,0), (-1,0)] # Right, left, down, up
        
        heapq.heappush(heap, (0,0,0))
        while heap:
            times, y, x = heapq.heappop(heap)

            # Find the shortest route.
            if (y,x)  == (n-1, m-1):
                return times
            
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < m:
                    nextTime = max(times, moveTime[ny][nx] ) + 1
                    if nextTime < minTime[ny][nx]:
                        minTime[ny][nx] = nextTime
                        
                        heapq.heappush(heap, (nextTime, ny, nx))

        return -1 # Can't reach

if __name__ == "__main__":
    sol = Solution()
    test = [[0,4,5],[4,4,5],[5,5,5]]
    print(sol.minTimeToReach(moveTime=test))