class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        """
        Find the maximum Manhattan distance from the origin that can be achieved at any time
        while performing the movements in "order".

        Change at most k characters to any of the four directions.
        1 <= s.length <= 10**5

        Manhattan distance = |x1 - x2| + |y1 - y2|
        """
        north = south = east = west = 0
        ans = 0
        for i in range(len(s)):
            direct = s[i]
            if direct == "N":
                north += 1
            elif direct == "S":
                south += 1
            elif direct == "E":
                east += 1
            elif direct == "W":
                west += 1
            
            Manhattan = abs(north - south) + abs(east - west)
            # Try convert k direction
            ## Each convert can let distance + 2
            ## Current movement (i + 1) - Manhattan = Possible effective dist
            dist = Manhattan + min(2 * k, i + 1 - Manhattan)
            ans = max(dist, ans)
        return ans

if __name__ == "__main__":
    sol = Solution()
    s = "NWSE"
    k = 1
    print(sol.maxDistance(s, k))