from itertools import combinations

class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word

        n = len(word)
        length = n - numFriends + 1
        max_char = max(word)
        result = ""

        for i in range(n):
            if word[i] == max_char:
                substr = word[i:i + length]
                result = max(result, substr)

        return result


if __name__ == "__main__":
    sol = Solution()
    word = "dbca"
    numFriends = 2
    print(sol.answerString(word, numFriends))