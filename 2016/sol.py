from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        """
        Return the maximum difference. If no such i and j exists, return -1.
        2 <= n <= 1000
        1 <= nums[i] <= 10**9
        0 <= i < j < n
        """
        max_diff = -1
        min_num = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > min_num:
                max_diff = max(max_diff, nums[i] - min_num)
            else:
                min_num = nums[i] 
        return max_diff

if __name__ == "__main__" :
    sol = Solution()
    nums = [999,997,980,976,948,940,938,928,924,917,907,907,881,878,864,862,859,857,848,840,824,824,824,805,802,798,788,777,775,766,755,748,735,732,727,705,700,697,693,679,676,644,634,624,599,596,588,583,562,558,553,539,537,536,509,491,485,483,454,449,438,425,403,368,345,327,287,285,270,263,255,248,235,234,224,221,201,189,187,183,179,168,155,153,150,144,107,102,102,87,80,57,55,49,48,45,26,26,23,15]
    print(sol.maximumDifference(nums))