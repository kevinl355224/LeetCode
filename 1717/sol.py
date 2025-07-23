class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        """
        Return the maximum points you can gain after applying the above operations on s.
        Remove substring "ab" and gain x points
        Remove substring "ba" and gain y points

        1 <= s.length <= 10**5
        1 <= x, y <= 10**4
        """

        def remove_word(s, first, second, point) -> tuple[str, int]:
            score = 0
            stack = []
            for letter in s:
                if stack and stack[-1] == first and letter == second:
                    stack.pop()
                    score += point
                else:
                    stack.append(letter)
            return stack, score
        if x > y:
            # Remove "ab" first
            remain_stack, score_1 = remove_word(s, "a", "b", x)
            _, score_2 = remove_word(remain_stack, "b", "a", y)
        else:
            # Remove "ba" first
            remain_stack, score_1 = remove_word(s, "b", "a", y)
            _, score_2 = remove_word(remain_stack, "a", "b", x)

        return score_1 + score_2

if __name__ == "__main__":
    sol = Solution()
    s = "cdbcbbaaabab"
    x = 4
    y = 5
    print(sol.maximumGain(s, x, y))