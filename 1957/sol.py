class Solution:
    def makeFancyString(self, s: str) -> str:
        """
        A fancy string is a string where no three consecutive characters are equal.
        Delete the minimum possible number of characters from s to make it fancy.
        Return the final string
        """
        # One line
        # return s[:2]  + "".join([s[i] for i in range(2, len(s)) if s[i] != s[i-1] or s[i] !=s[i-2]])

        # Faster
        ans = list(s[:2])

        for c in s[2:]:
            if c == ans[-1] and c == ans[-2]:
                continue
            else:
                ans.append(c)
        
        return "".join(ans)
        

if __name__ == "__main__":
    sol = Solution()
    s = "eeetcode"
    print(sol.makeFancyString(s))