from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        """
        Return the count of square that can created by two point.
        Point must on top-left and bottom-right.
        Each square can't include other point.
        
        2 <= n <= 50
        points[i].length == 2
        0 <= points[i][0], points[i][1] <= 50
        """
        cnt = 0
        points.sort(key=lambda x: (x[0], -x[1]))

        for i, (_, top) in enumerate(points):
            bot = float("-inf")
            for (_, y) in points[i +1 :]:
                if bot < y <= top:
                    cnt += 1
                    bot = y
                    if top == bot:
                        break
        return cnt
    
if __name__ == "__main__":
    sol = Solution()
    points = [[1,1],[2,2],[3,3]]
    print(sol.numberOfPairs(points))