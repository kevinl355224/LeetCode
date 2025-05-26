from typing import List
from collections import deque

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        length = len(colors)
        adjacent_map = [[] for _ in range(length)]
        indeg = [0] * length
        for start, end in edges:
            adjacent_map[start].append(end)
            indeg[end] += 1

        dp = [[0] * 26 for _ in range(length)]
        q = deque()
        for node in range(length):
            if indeg[node] == 0:
                # Start from end
                q.append(node)
                dp[node][ord(colors[node]) - 97] = 1

        visited, res = 0, 0
        while q:
            node = q.popleft()
            visited += 1
            res = max(res, max(dp[node]))
            for adjacent in adjacent_map[node]:
                color_idx = ord(colors[adjacent]) - 97
                for color in range(26):
                    val = dp[node][color] + (1 if color == color_idx else 0)
                    if val > dp[adjacent][color]:
                        dp[adjacent][color] = val
                indeg[adjacent] -= 1
                # When all previous node is consider. Add to queue
                if indeg[adjacent] == 0:
                    q.append(adjacent)

        return res if visited == length else -1