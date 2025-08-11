from typing import List

class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        """
        Start from
        (0, 0) : (i + 1, j + 1), (i + 1, j), (i, j + 1)
        (0, n - 1) : (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)
        (n - 1, 0) : (i - 1, j + 1), (i, j + 1), (i + 1, j + 1)
        
        Exactly n - 1 moves according to the following rules to reach the room (n - 1, n - 1)

        Return the maximum number of fruits the children can collect from the dungeon.

        2 <= n == fruits.length == fruits[i].length <= 1000
        0 <= fruits[i][j] <= 1000
        """
        # Because can only move n-1 step, the person from (0,0) can only move (i + 1, j + 1)
        size = len(fruits)
        total = 0
        for i in range(size):
            total += fruits[i][i]
        # print(total)

        # Fruit number with three directions. 
        # right_path[-1], [-2] is to prevent. Beyond the border
        right_path = [fruits[size - 1][0], 0, 0] 
        
        bottom_path = [fruits[0][size - 1], 0, 0]
        window = 2
        mid = size // 2
        # Use DP 
        for i in range(1, size - 1):
            new_right = [0] * (window + 2)
            new_bottom = [0] * (window + 2)
            
            for j in range(window):
                # Right path
                new_right[j] = max(right_path[j - 1], right_path[j], right_path[j + 1]) + fruits[i][size - 1 - j]
                # bottom path
                new_bottom[j] = max(bottom_path[j - 1], bottom_path[j], bottom_path[j + 1]) + fruits[size - 1 - j][i]

            # update
            right_path = new_right
            bottom_path = new_bottom

            # the max window size is at mid of the size
            if i < mid:
                window += 1
            elif i > mid:
                window -= 1
        
        return total + bottom_path[0] + right_path[0]

if __name__ == "__main__":
    sol = Solution()
    fruits = [[1,2,3,4],[5,6,8,7],[9,10,11,12],[13,14,15,16]]
    print(sol.maxCollectedFruits(fruits))