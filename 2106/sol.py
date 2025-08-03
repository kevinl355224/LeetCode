from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        """
        Fruits[i] = [positioni, amounti]
        Fruits is already sorted by positioni in ascending order
        You are at the position startPos
        Can walk at most k steps

        Return the maximum total number of fruits you can harvest.

        0 <= startPos, positioni <= 2 * 10**5
        1 <= fruits.length <= 10**5
        1 <= amounti <= 10**4
        0 <= k <= 2 * 10**5
        """
        n = len(fruits)
        
        # Extract positions and compute prefix sum of fruit amounts
        pos = [fruits[i][0] for i in range(n)]
        preSum = [0] * (n + 1)
        for i in range(n):
            preSum[i + 1] = preSum[i] + fruits[i][1]

        maxFruits = 0
        left = 0

        # Use a sliding window [left, right]
        for right in range(n):
            leftPos = fruits[left][0]
            rightPos = fruits[right][0]

            # Two walking strategies:
            # 1. Go left first, then right (total distance = |start-left| + (right-left))
            dist1 = abs(startPos - leftPos) + (rightPos - leftPos)

            # 2. Go right first, then left (total distance = |start-right| + (right-left))
            dist2 = abs(startPos - rightPos) + (rightPos - leftPos)

            # Shrink window from the left if both strategies exceed k steps
            while left <= right and min(dist1, dist2) > k:
                left += 1
                if left <= right:
                    leftPos = fruits[left][0]
                    dist1 = abs(startPos - leftPos) + (rightPos - leftPos)
                    dist2 = abs(startPos - rightPos) + (rightPos - leftPos)

            # If the window is valid, calculate total fruits collected
            if left <= right:
                totalFruits = preSum[right + 1] - preSum[left]
                maxFruits = max(maxFruits, totalFruits)

        return maxFruits


    
if __name__ == "__main__":
    sol = Solution()
    fruits = [[1,8],[2,8],[4,20],[6,1],[8,100]]
    startPos = 5
    k = 5
    print(sol.maxTotalFruits(fruits, startPos, k))
