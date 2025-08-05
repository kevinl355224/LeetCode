from typing import List
from collections import defaultdict

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        """
        fruits[i] represents the quantity of the ith type of fruit
        baskets[j] represents the capacity of the jth basket.

        From left to right
        Each fruit type must be placed in the leftmost available basket with a capacity 
        greater than or equal to the quantity of that fruit type.
        
        Each basket can hold only one type of fruit.
        If a fruit type cannot be placed in any basket, it remains unplaced.

        Return the number of fruit types that remain unplaced after all possible allocations are made.

        n == fruits.length == baskets.length
        1 <= n <= 100
        1 <= fruits[i], baskets[i] <= 1000
        """

        for fruit in fruits:
            # Search basket for fruit
            for basket in baskets:
                if basket >= fruit:
                    baskets.remove(basket)
                    break
        return len(baskets)


if __name__ == "__main__":
    sol = Solution()
    fruits = [4,2,5]
    baskets = [3,5,4]
    print(sol.numOfUnplacedFruits(fruits, baskets))