from typing import List
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for i, word in enumerate(words):
            if x in word:
                ans.append(i)
        return ans
    
if __name__ == "__main__":
    words = ["leet","code"]
    x = "e"
    sol = Solution()
    print(sol.findWordsContaining(words, x))
