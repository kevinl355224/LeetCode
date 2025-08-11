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
        powers_MOD = {} # All powers divide by MOD
        base = 0
        while n:
            if n & 1:
                powers.append(base)
                powers_MOD[base] = (1 << base) % MOD
            base += 1
            n >>= 1

        # print(powers)
        # print(powers_MOD)

        answers = [0] * len(queries)

        for i, (a, b) in enumerate(queries):
            expo = sum(powers[a:b]) + powers[b]
            if expo not in powers_MOD:
                powers_MOD[expo] = (1 << expo) % MOD
            answers[i] = powers_MOD[expo]

        return answers

if __name__ == "__main__":
    sol = Solution()
    n = 15
    queries = [[0,1],[2,2],[0,3]]
    print(sol.productQueries(n, queries))