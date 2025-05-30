from typing import List

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        """
        edges = [2,2,3,-1]
        node1, node2 = 0, 1
        Find x which max(dist(node1 → x), dist(node2 → x)) is minimized
        return the node with the smallest index, 
        and if no possible answer exists, return -1.
        (1) -> a -> b <- c <- (2) Find can "be reached"
        Find the smallest difference between node1 and each others.
        Find the smallest difference between node2 and each others.
        max(result1, result2)

        2 <= n <= 10**5
        """
        n = len(edges)
        path = {}
        for idx in range(n):
            path[idx] = edges[idx]

        visit1 = set() # Save the node been visit by path 1 or 2
        visit2 = set()
        ans1 = float("inf")
        ans2 = float("inf")
        while node1 != -1 or node2 != -1:
            if node1 != -1:
                if node1 in visit2:
                    ans1 = node1
                if node1 not in visit1:
                    visit1.add(node1)
                    node1 = path[node1] # Walk to next node start from node1
                else:
                    node1 = -1

            if node2 != -1:
                if node2 in visit1:
                    ans2 = node2
                if node2 not in visit2:
                    visit2.add(node2)
                    node2 = path[node2] # Walk to next node start from node2
                else:
                    node2 = -1
            if ans1 != float("inf") or ans2 != float("inf"):
                return int(min(ans1, ans2))
        return -1

if __name__ == "__main__":
    edges = [4,4,8,-1,9,8,4,4,1,1]
    node1 = 5
    node2 = 6
    sol = Solution()
    print(sol.closestMeetingNode(edges, node1, node2))
