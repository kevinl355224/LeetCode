from typing import List
from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        """
        max(subsequences) - min(subsequences) = 1
        return the length of its longest subsequences

        1 <= nums.length <= 2 * 10**4
        -10**9 <= nums[i] <= 10**9
        """
        max_length = 0

        cnt_dict = Counter(nums)

        ordered_tuple = [(num, cnt) for num, cnt in cnt_dict.items()]
        ordered_tuple.sort(key=lambda x: x[0])
        # print(ordered_tuple)
        for i in range(1, len(ordered_tuple)):
            if ordered_tuple[i][0] - ordered_tuple[i-1][0] == 1:
                max_length = max(max_length, ordered_tuple[i][1] + ordered_tuple[i-1][1])

        return max_length

if __name__ == "__main__":
    sol = Solution()
    nums = [1,3,2,2,5,2,3,7]
    print(sol.findLHS(nums))