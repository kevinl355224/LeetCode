from typing import List

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        """
        Return the earliest and the latest possible round number
        2 <= n <= 28
        1 <= firstPlayer < secondPlayer <= n

        [1,2,3,4,5,6,7,8,9,10,11]
           *   *

        Every round can drop half of number (n+1)//2
        The earlest:
            Let the first num left == right num right
        """
        def dfs(n, p1, p2):
            if p1 + p2 == n + 1:
                return (1, 1)
            if p1 > p2:
                p1, p2 = p2, p1
            if n <= 4:
                return (2, 2)
            
            m = (n + 1) // 2
            minR, maxR = float("inf"), float("-inf")
            # If player on p1 left side > player on p2 right side 
            # [1,2,3,4,5,6,7,8,9,10,11] -> [1,2,3,4,5,6,7,8,9,10,11]
            #                *    *           *   *
            if p1 - 1 > n - p2:
                t = n + 1 - p1
                p1 = n + 1 - p2
                p2 = t

            # If p2 on the left side
            if p2 * 2 <= n + 1:
                a = p1 - 1
                b = p2 - p1 - 1

                for i in range(a + 1):
                    for j in range(b + 1):
                        r1, r2 = dfs(m, i + 1, i + j + 2)
                        minR = min(minR, r1 + 1)
                        maxR = max(maxR, r2 + 1)
            # IF p2 on the right side
            else:
                p4 = n + 1 - p2
                a = p1 - 1
                b = p4 - p1 - 1
                c = p2 - p4 - 1

                for i in range(a + 1):
                    for j in range(b + 1):
                        offset = i + j + 1 + (c + 1) // 2 + 1
                        r1, r2 = dfs(m, i + 1, offset)
                        minR = min(minR, r1 + 1)
                        maxR = max(maxR, r2 + 1)

            # Step 4: Return earliest and latest round
            return (minR, maxR)
        return list(dfs(n, firstPlayer, secondPlayer))
    
if __name__ == "__main__":
    n = 11
    firstPlayer = 2
    secondPlayer = 4
    sol = Solution()
    print(sol.earliestAndLatest(n, firstPlayer, secondPlayer))