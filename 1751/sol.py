import bisect
from typing import List

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        """
        Each list is an event. Include start_day, end_day and value
        k represents the maximum number of events you can attend.

        Can only attend a event in one time and must attend the entire event.

        Return the maximum sum of values that you can receive by attending events.

        1 <= k * events.length <= 10**6
        1 <= startDayi <= endDayi <= 10**9
        1 <= valuei <= 10**6
        """
        dp = [[0] * (k + 1) for _ in events] # row: event column: num of attended
        
        # Start from first event. Update dp.
        events.sort(key=lambda x :x[1])
        end_days = [event[1] for event in events]
        
        for i in range(len(events)):
            # Get the index j which means the end day of j won't conflict with start day of i
            pre = bisect.bisect_right(end_days, events[i][0] - 1) - 1
            for j in range(1, k + 1):
                if j == 1:
                    val = events[i][2]
                else:   # There is no event before event i. So it's impossible attended more than 1 event. 
                    if pre ==-1:
                        val = 0
                    else:
                        val = dp[pre][j-1] + events[i][2]

                if i == 0:
                    dp[i][j] = max(dp[i][j], val)
                else:
                    dp[i][j] = max(
                        dp[i-1][j],     # The value if not attend event i
                        val         # The value if attend event i
                    )

        ans = 0
        for i in range(len(events)):
            for j in range(1, k + 1):
                ans = max(ans, dp[i][j])
        return ans

if __name__ == "__main__":
    sol = Solution()
    events = [[1, 2, 4], [2, 3, 10], [3, 4, 3]]
    k = 2
    print(sol.maxValue(events, k))
