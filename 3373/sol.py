from typing import List
from collections import defaultdict

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        """
        Connect one node tree1[u] to tree2[v]
        Start from tree1[u] to any node if distance is even
        node is always target to itself.
        
        There two color in tree if yellow and blue.
        When you choice a yellow node. The distance between all blue node will be odd.
        On the other side, distance between all yellow will be even.

        ans = (The num of choiced color) + (the larger num of color in tree2))
        """
        n, m=len(edges1) + 1, len(edges2) + 1
        adj1=[[] for _ in range(n)]
        adj2=[[] for _ in range(m)]
        mod=[False]*n # Used to remember odd or even in tree1

        def build_adj(edges, adj):
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)

        # dfs for tree 1
        def dfs(i, parent, isEven, adj):
            cnt = isEven
            mod[i] = isEven
            for j in adj[i]:
                if j == parent: continue
                cnt += dfs(j, i, not isEven, adj)
            return cnt
        
        # dfs for tree 2
        def dfs0(i, parent, isEven, adj): 
            cnt = isEven
            for j in adj[i]:
                if j == parent: continue
                cnt += dfs0(j, i, not isEven, adj)
            return cnt
        
        build_adj(edges1, adj1)
        build_adj(edges2, adj2)
        y = dfs0(0, -1, True, adj2) # The start node is even
        x = dfs(0, -1, True, adj1)

        maxCount2 = max(y, m-y) # max(even, numOfNode - even = odd)
        count = ((n - x) + maxCount2, x + maxCount2)
        return [count[b] for b in mod]


if __name__ == "__main__":
    sol = Solution()
    edges1 = [[0,1],[0,2],[2,3],[2,4]]
    edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
    print(sol.maxTargetNodes(edges1, edges2))