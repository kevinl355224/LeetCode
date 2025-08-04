from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        Two baskets, and each basket can only hold a single type of fruit. 
        There is no limit on the amount of fruit each basket can hold.

        fruits[i] is the type of fruit the ith tree produces.
        
        Return the maximum number of fruits you can pick.

        1 <= fruits.length <= 105
        1 <= fruits.length <= 10**5
        """
        # Use two pointer
        max_amount = cnt = 0
        pointer1 = pointer2 = [-1, -1] # [type, closet position]

        for i in range(len(fruits)):

            if fruits[i] == pointer1[0]:
                pointer1[1] = i
                cnt += 1
            elif fruits[i] == pointer2[0]:
                pointer2[1] = i
                cnt += 1
            else:
                max_amount = max(max_amount, cnt)
                # Select the pointer which is far from i
                if pointer1[1] < pointer2[1]:
                    cnt = i - pointer1[1]
                    pointer1 = [fruits[i], i]
                else:
                    cnt = i - pointer2[1]
                    pointer2 = [fruits[i], i]

        return max(max_amount, cnt)


if __name__ == "__main__":
    sol = Solution()
    fruits = [0,1,2,2]
    print(sol.totalFruit(fruits))