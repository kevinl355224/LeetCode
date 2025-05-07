import heapq
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # n(y)*m(x)
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
