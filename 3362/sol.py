from typing import List
import heapq

import heapq

class Solution:
    def maxRemoval(self, nums, queries):
        """
            ------->
        nums     [a, b, c, d, e, f, g, ...]
        query 0  [0__1]  
              1    [1_____3]
              2  [0______________6] <--- l = idx(0) and longest
                  ^
                Try make num[0] to 0
                Put query l = idx(0) into available
                Pick longest query[2] to substract num[0]
        """

        n = len(nums)
        m = len(queries)
        diff = [0] * (n + 1)

        queries.sort()
        available = []  # Max heap via negatives
        q_index = 0

        for n in range(n):
            # recover prefix sum
            if n > 0:
                diff[n] += diff[n - 1]

            # Put all query l equal to n into available
            while q_index < m and queries[q_index][0] == n:
                heapq.heappush(available, -queries[q_index][1]) # save and let big array be small value
                q_index += 1

            # If nums[n] is bigger than diff[n] try get longer query in availible
            while diff[n] < nums[n]:
                # If no query or the nex avaliable query r can't reach n.
                if not available or -available[0] < n:
                    return -1

                diff[n] += 1
                end_n = -heapq.heappop(available)
                if end_n + 1 < len(diff):
                    diff[end_n + 1] -= 1
            # available is remaining query
        return len(available)

if __name__ == "__main__":
    sol = Solution()
    nums = [0,0,1,1,0,0]
    queries = [[2,3],[0,2],[3,5]]
    print(sol.maxRemoval(nums, queries))