from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        """
        eturn the number of distinct bitwise ORs of all the non-empty subarrays of arr.

        1 <= arr.length <= 5 * 10**4
        0 <= arr[i] <= 10**9
        """

        seen = set()
        previous_set = set()
        # Sliding window
        for n in arr:
            current_set = {n}
            for m in previous_set:
                value = m | n
                current_set.add(value)
            #current_set = {n} | {m | n for m in previous_set}

            previous_set = current_set
            seen |= previous_set
            
        return len(seen)

if __name__ == "__main__":
    sol = Solution()
    arr = [1,2,4,9]
    print(sol.subarrayBitwiseORs(arr))