from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        maxFruits = 0
        left_idx = 0
        current = 0

        # Sliding window with double pointer
        for right_idx in range(len(fruits)):
            current += fruits[right_idx][1]
            
            while left_idx <= right_idx:
                left = fruits[left_idx][0]
                right = fruits[right_idx][0]
                # The min step could be
                steps = min(abs(startPos - left) + (right - left), 
                            abs(right - startPos) + (right - left))
                
                if steps <= k:
                    break
                else:
                    current -= fruits[left_idx][1]
                    left_idx += 1
            maxFruits = max(maxFruits, current)

        return maxFruits

    
if __name__ == "__main__":
    sol = Solution()
    fruits = [[1,8],[2,8],[4,20],[6,1],[8,100]]
    startPos = 5
    k = 5
    print(sol.maxTotalFruits(fruits, startPos, k))
