import heapq
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        """
        1 <= n <= 100
        1 <= meetings.length <= 10**5

        Return the number of the room that held the most meetings. 
        If there are multiple rooms, return the room with the lowest number.
        """
        meetings.sort(key=lambda x: x[0])

        use_cnt = [0] * n # room number : used times
        occupied_romm_q = [] # A queue record the status of room (end time, room number)
        avalible_romm_q = list(range(n)) # [room number, ]
        
        for start, end in meetings:
            # Check if any meeting has been done
            while occupied_romm_q and occupied_romm_q[0][0] <= start:
                end_time, room_number = heapq.heappop(occupied_romm_q)
                heapq.heappush(avalible_romm_q, room_number)

            if avalible_romm_q:
                # Assign meeting to the smallest-numbered available room
                room_number = heapq.heappop(avalible_romm_q)
                heapq.heappush(occupied_romm_q, (end, room_number))
            else:
                # No room available, delay the meeting to the earliest ending room
                earliest_end, room_number = heapq.heappop(occupied_romm_q)
                heapq.heappush(occupied_romm_q, (earliest_end + end - start, room_number))

            use_cnt[room_number] += 1

        # print(use_cnt)

        max_meetings = max(use_cnt)
        for i, cnt in enumerate(use_cnt):
            if cnt == max_meetings:
                return i


if __name__ == "__main__":
    sol = Solution()
    n = 2
    meetings = [[10,11],[2,10],[1,17],[9,13],[18,20]]

    print(sol.mostBooked(n, meetings))