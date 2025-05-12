from typing import List

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # [2,1,3,0]
        # Zero can't be the first digit
        # Last digit must be even
        # Concatenation of three digit ex. 132,120,312...

        ans = [0]*1000
        amount = 0
        count = [0]*10
        for i in digits:
            count[i] += 1
        
        # First digit
        for a in range(1,10):
            if not count[a]:
                continue
            # Second digit
            temp_a = count[:]
            temp_a[a] -= 1
            for b in range(10):
                if not temp_a[b]:
                    continue
                temp_b = temp_a[:]
                temp_b[b] -= 1
                # Third digit
                for c in range(0,10,2):
                    if not temp_b[c]:
                        continue
                    # Found number
                    ans[amount] = a*100 + b*10 + c
                    amount += 1
        return ans[:amount]

if __name__ == "__main__":
    sol = Solution()
    print(sol.findEvenNumbers(digits=[2,1,3,0]))