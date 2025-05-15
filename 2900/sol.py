from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        # words = ["e","a","b"]
        # groups = [0,0,1]
        prev_groups = groups[0]
        ans = [words[0]]
        for n in range(1, len(words)):
            if groups[n] != prev_groups:
                ans.append(words[n])
                prev_groups = groups[n]
        return ans

if __name__ == "__main__":
    words = ["e","a","b"]
    groups = [0,0,1]
    sol = Solution()
    print(sol.getLongestSubsequence(words, groups))
