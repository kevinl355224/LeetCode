from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]: 
        """
        Given the string s, the size of each group k and the character fill,
        return a string array denoting the composition of every group s has been divided into.

        1 <= s.length <= 100
        """
        ans = [s[i:i+k] for i in range(0, len(s), k)]
        ans[-1] += fill * (k - len(ans[-1]))
        return ans
    
if __name__ == "__main__":
    sol = Solution()
    s = "abcdefghih"
    k = 3
    fill = "x" 
    print(sol.divideString(s, k, fill))
