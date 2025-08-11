from typing import List

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        """
        powers is composed of the minimum number of powers of 2 that sum to n
        queries[i] = [lefti, righti]
        Each queries[i] represents a query where you have to find the product of all powers[j] with lefti <= j <= righti.
        Return answers[i] which is the answer to the ith query.
        1 <= n <= 10**9
        1 <= queries.length <= 10**5
        """
        MOD = 10 ** 9 + 7
        # get powers
        powers = [] 
        base = 0
        while n:
            if n & 1:
                powers.append(1 << base)
            base += 1
            n >>= 1
        # print(powers)

        answers = [0] * len(queries)
        m = len(powers)
        results = [[0] * m for _ in range(m)] # [start][end]
        for i in range(m):
            cur = 1
            for j in range(i, m):
                cur = cur * powers[j] % MOD
                results[i][j] = cur

        for idx, (a, b) in enumerate(queries):
            answers[idx] = results[a][b]

        return answers

if __name__ == "__main__":
    sol = Solution()
    n = 15
    queries = [[0,1],[2,2],[0,3]]
    print(sol.productQueries(n, queries))