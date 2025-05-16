import heapq
from typing import List
"""
    From solution
    Save the pattern first
"""
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        if n == 0: return []

        dp = [1] * n
        prev = [-1] * n
        patterns = {}
        max_len, max_idx = 1, 0

        for i, w in enumerate(words):
            best_len, best_prev = 1, -1
            g_i, L = groups[i], len(w)
        
            # Generate all patterns for current word by replacing one character with '*'
            # {'*db': [0], 'b*b': [0], 'bd*': [0]}
            for j in range(L):
                patt = w[:j] + '*' + w[j+1:]
                for k in patterns.get(patt, ()):
                    if groups[k] != g_i and dp[k] + 1 > best_len:
                        best_len = dp[k] + 1
                        best_prev = k

            dp[i] = best_len
            prev[i] = best_prev
            
            for j in range(L):
                patt = w[:j] + '*' + w[j+1:]
                patterns.setdefault(patt, []).append(i)
            if best_len > max_len:
                max_len = best_len
                max_idx = i

        res, cur = [], max_idx
        while cur != -1:
            res.append(words[cur])
            cur = prev[cur]

        return res[::-1]


if __name__ == "__main__":
    words = ["bdb","aaa","ada"]
    groups = [2,1,3]
    sol = Solution()
    print(sol.getWordsInLongestSubsequence(words, groups))
