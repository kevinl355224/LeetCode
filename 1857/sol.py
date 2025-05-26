from typing import List
from functools import lru_cache 
from collections import defaultdict

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        """
        colors = a-z
        ord(a) = 97
        """
        
        lenght = len(colors)
        dp = [[0] * 26 for _ in range(lenght)] # [node][color] = num
        # Walkthrough path
        visit = set()
        path = set()
        adjacent_map = defaultdict(list)

        for edge in edges:
            adjacent_map[edge[0]].append(edge[1])

        @lru_cache(None)
        def dfs(node):
            if node in path:
                return float("inf")
            if node in visit:
                return 0
            visit.add(node)
            path.add(node)

            colorIdx = ord(colors[node]) - ord("a")
            dp[node][colorIdx] = 1

            for adjacent in adjacent_map[node]:
                if dfs(adjacent) == float("inf"):
                    return float("inf")
                for color in range(26):
                    dp[node][color] = max(dp[adjacent][color] + (1 if color == colorIdx else 0),
                                          dp[node][color])
            path.remove(node)
            return max(dp[node])

        result = 0
        for node in range(lenght):
            result = max(dfs(node), result)

        return -1 if result == float("inf") else result

if __name__ == "__main__":
    sol = Solution()
    colors = "abaca"
    edges = [[0,1],[0,2],[2,3],[3,4]]
    print(sol.largestPathValue(colors, edges))