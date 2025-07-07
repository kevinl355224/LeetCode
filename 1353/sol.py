from typing import List
import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        """
        Each list is a event, and has a start day and end day.
        Return the maximum number of events you can attend.

        1 <= events.length <= 10**5
        events[i].length == 2
        1 <= startDayi <= endDayi <= 10**5
        """
        # Keep select the shortest left day.
        events.sort()
        day = 1
        num_event = len(events)
        i = 0 # Point to the un-processed event
        q = [] # Use to save current can attend event
        cnt = 0

        while i < num_event or q:
            # Add attendable event in to q
            while i < num_event and events[i][0] <= day:
                heapq.heappush(q, events[i][1])
                i += 1

            # Remove the expired event
            while q and q[0] < day:
                heapq.heappop(q)
            
            # select a event and day plus 1

            if q:
                heapq.heappop(q)
                cnt += 1
            
            day += 1
        return cnt


if __name__ == "__main__":
    sol = Solution()
    events = [[1,2],[2,3],[3,4]]
    print(sol.maxEvents(events))