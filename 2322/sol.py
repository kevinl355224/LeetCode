from typing import List
from collections import defaultdict

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        """
        Remove two distinct edges of the tree to form three connected components.

        score = max_xor - min_xor
        Return the minimum score of any possible pair of edge removals on the given tree.

        n == nums.length
        3 <= n <= 1000
        1 <= nums[i] <= 10**8
        """
        # Init
        n = len(nums)
        subtree_xor = [0] * n
        parents = [-1] * n
        tree = defaultdict(list)

        in_time = [0] * n # When start process node
        out_time = [0] * n # When finish all its child node
        time = 0
        for i, j in edges:
            tree[i].append(j)
            tree[j].append(i)
        # print(tree)

        # Build subtree_xor, parent, in_time and out_time.
        def dfs(node: int, par: int):
            nonlocal time
            parents[node] = par
            in_time[node] = time
            time += 1
            xor = nums[node]
            for nei in tree[node]:
                if nei != par:
                    xor ^= dfs(nei, node)
            out_time[node] = time
            subtree_xor[node] = xor
            return xor
        
        total_xor = dfs(0, -1)
        # print(subtree_xor)
        # print(total_xor)
        # print("in_time ",in_time)
        # print("out_time", out_time)

        # Convert the edges to be directed from parent to child
        # Build a list of child nodes that represent directed edges from parent[i] -> i.
        # Ex.    edges = [[0,1],[1,2],[1,3],[3,4]]
        #   edge_nodes = [   1,    2,    3,    4 ] (Pick child to represent the edge)
        edge_nodes = [] 
        for i in range(n):
            if parents[i] != -1:
                edge_nodes.append(i) # i is a child node; the edge is from parent[i] to i

        res = float('inf')

        def is_ancestor(a: int, b: int) -> bool:
            # Node `a` is an ancestor of node `b` if:
            # 1. `a`'s in_time is before `b`'s in_time (i.e., DFS entered `a` before `b`)
            # 2. `a`'s out_time is after or equal to `b`'s out_time (i.e., DFS exited `a` after `b`)
            # This means `b` lies within the DFS subtree rooted at `a`
            return in_time[a] < in_time[b] and out_time[b] <= out_time[a]

        # Iterate over all unique pairs of edges
        for i in range(len(edge_nodes)):
            for j in range(i + 1, len(edge_nodes)):
                c1 = edge_nodes[i]
                c2 = edge_nodes[j]

                if is_ancestor(c1, c2):
                    # C1 is c2's ancestor. c2 is the longerst child tree
                    xor1 = subtree_xor[c2]
                    xor2 = subtree_xor[c1] ^ xor1
                    xor3 = total_xor ^ subtree_xor[c1]
                elif is_ancestor(c2, c1):
                    xor1 = subtree_xor[c1]
                    xor2 = subtree_xor[c2] ^ xor1
                    xor3 = total_xor ^ subtree_xor[c2]
                else:
                    xor1 = subtree_xor[c1]
                    xor2 = subtree_xor[c2]
                    xor3 = total_xor ^ xor1 ^ xor2

                score = max(xor1, xor2, xor3) - min(xor1, xor2, xor3)
                res = min(res, score)

        return res


if __name__ == "__main__":
    sol = Solution()
    nums = [1,5,5,4,11] 
    edges = [[0,1],[1,2],[1,3],[3,4]]
    print(sol.minimumScore(nums, edges))