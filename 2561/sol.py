from typing import List
from collections import Counter

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        """
        Swap num betewen basket 1 and 2 makes them exactly the same baskets.

        Swap cost = min(basket1[i], basket2[j]) 

        Return the minimum cost to make both the baskets equal or -1 if impossible.

        1 <= basket1.length <= 10**5
        1 <= basket1[i],basket2[i] <= 10**9
        """
        # To minimize cost. use little to change big num.
        count1 = Counter(basket1)
        count2 = Counter(basket2)

        # print(count1, count2)

        swap1, swap2 = [], []

        # List the num which should swap to another basket.
        for n in set(basket1) | set(basket2):
            
            diff = count1[n] - count2[n]
            # If diff is odd return -1
            if diff & 1:
                return -1

            if diff > 0:
                swap1.extend([n] * (diff // 2))
            elif diff < 0:
                swap2.extend([n] * (-diff // 2))

        if not swap2:
            return 0

        total = 0
        # Use min num as a temp changer
        min_cost = min(min(basket1), min(basket2)) * 2

        swap1.sort()
        swap2.sort(reverse=True)

        left, right = 0, len(swap1) - 1
        # keep calculate the cost from left
        cost = 0
        while left < len(swap1):
            cost = min(swap1[left], swap2[left])
            if cost <= min_cost:
                total += cost
                left += 1
            else:
                break

        # keep calculate the cost from right
        cost = 0
        while right > left:
            cost = min(swap1[right], swap2[right])
            if cost <= min_cost:
                total += cost
                right -= 1
            else:
                break

        # Calculate the mid part
        total += (min_cost * (right - left + 1))

        return total
    
if __name__ == "__main__":
    sol = Solution()
    basket1 = [2,2,9,8,8,5,6,7,7]
    basket2 = [6,6,5,6,3,9,5,3,5]
    print(sol.minCost(basket1, basket2))