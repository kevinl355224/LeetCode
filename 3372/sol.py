from typing import List

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        """
        u -> v if  number between edges[u], edges[v] <= k
        Combine one node[i] from tree1 to tree2
        Start from node[i]. How many path is <= k
        """
        
        


if __name__ == "__main__":
    edges1 = [[0,1],[0,2],[2,3],[2,4]]
    edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]

    sol = Solution()
    print(sol.maxTargetNodes(edges1,edges2))
