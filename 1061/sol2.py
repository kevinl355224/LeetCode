class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        """
        Union-Find (Disjoint Set Union, DSU)
        """
        parent = list(range(26))  # Union-Find: index 0 = "a", ..., 25 = "z"

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                if px < py: # ans is find smallest
                    parent[py] = px
                else:
                    parent[px] = py

        for a, b in zip(s1, s2):
            union(ord(a) - ord("a"), ord(b) - ord("a"))

        result = []
        for ch in baseStr:
            rep = find(ord(ch) - ord("a"))
            result.append(chr(rep + ord("a")))

        return "".join(result)
