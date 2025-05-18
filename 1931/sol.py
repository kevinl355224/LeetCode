class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        # A m*n grid
        # 0: red, 1: green, 2:blue
        # Return the number of ways to color the grid with no two adjacent cells having the same color.

        # Count all possible states into base-3 encoding
        def dfs(pos, prev_color, mask):
            # print(f"pos: {pos}, prev: {prev_color}, mask: {mask}")
            if pos == m:
                states.append(mask)
                return
            for color in range(3):
                if color != prev_color:
                    dfs(pos + 1, color, mask * 3 + color)

        MOD, states = 10**9 + 7, []
        dfs(0, -1, 0)
        S = len(states)
        compat = [[] for _ in range(S)]

        # Compare two column states to see if they can be adjacent. If so, save the result into compat.
        for i, s1 in enumerate(states):
            for j, s2 in enumerate(states):
                x, y = s1, s2
                ok = True
                for _ in range(m):
                    if x % 3 == y % 3:
                        ok = False
                        break
                    x //= 3
                    y //= 3
                if ok:  compat[i].append(j)
        """
        When m = 2
        states = [1, 2, 3, 5, 6, 7]
        compat = [[2, 3, 4], [2, 4, 5], [0, 1, 5], [0, 4, 5], [0, 1, 3], [1, 2, 3]]
        compat[0] = [2, 3, 4] means that states[0] can be adjacent to states[2], states[3], and states[4]
        """

        dp = [1] * S
        for _ in range(n - 1):
            new_dp = [0] * S
            for i in range(S):
                if dp[i]:
                    for j in compat[i]:
                        # Accumulate the number of valid ways to reach state `j` in the next column
                        new_dp[j] = (new_dp[j] + dp[i]) % MOD
            dp = new_dp # Move to the next column

        """
        If states[0] = [0,1] and dp[0] = 3
        means that there are 3 different ways to build a valid grid of n columns,
        where the final (last) column has vertical colors [0,1],
        and all previous columns are valid and compatible (adjacent cells differ).
        """
        return sum(dp) % MOD 
    
if __name__ == "__main__":
    sol = Solution()
    m = 2
    n = 2
    print(sol.colorTheGrid(m=m, n=n))