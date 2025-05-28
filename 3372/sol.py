from typing import List
from collections import defaultdict, deque

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        """
        u -> v if  number between edges[u], edges[v] <= k
        Combine one node[i] from tree1 to tree2
        Start from node[i]. How many path is <= k
        """
        def dfs(node, parent, children, k):
            if k < 0:
                return 0
            res = 1
            for child in children[node]:
                if child == parent:
                    continue
                res += dfs(child, node, children, k-1)
            return res
        
        def build(edges, k):
            children = defaultdict(list)
            for a, b in edges:
                children[a].append(b)
                children[b].append(a)

            n = len(edges) + 1 # number of nodes
            res = [0] * n
            
            for i in range(n):
                res[i] = dfs(i, -1, children, k)
            return res
        
        n = len(edges1) + 1 # number of nodes
        count1 = build(edges1, k)
        count2 = build(edges2, k-1)

        maxCount2 = max(count2)
        ans = [count1[i] + maxCount2 for i in range(n)]
        return ans

if __name__ == "__main__":
    edges1 = [[0,1],[0,2],[2,3],[2,4]]
    edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
    k = 2
    sol = Solution()
    print(sol.maxTargetNodes(edges1,edges2,k))
