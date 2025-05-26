from collections import Counter
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        """
        Check every word, and check whether a palindrome in words
        """
        count_words = Counter(words)
        remaining_double_word = 0
        ans = 0
        for word, count in count_words.items():
            if word[0] == word[1]:
                if count & 1:
                    remaining_double_word += 1
                    ans = ans + count - 1
                else:
                    ans += count
                continue
            p_word = word[::-1]
            if word < p_word:
                ans += min(count ,count_words[p_word])*2

        if remaining_double_word >= 1:
            ans+=1

        return ans*2

if __name__ == "__main__":
  sol = Solution()
  words = ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]
  print(sol.longestPalindrome(words))
