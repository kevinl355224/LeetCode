from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """
        Erase a subarray containing unique elements.
        Return the maximum score you can get by erasing exactly one subarray.

        1 <= nums.length <= 10**5
        1 <= nums[i] <= 10**4
        """
        left = 0
        seen = set()
        max_sum = 0
        current_sum = 0
        
        for right in range(len(nums)):
            # Duplicate
            if nums[right] in seen:
                while nums[left] != nums[right]:
                    seen.remove(nums[left])
                    current_sum -= nums[left]
                    left += 1
                left += 1
            else:
                seen.add(nums[right])
                current_sum += nums[right]
                max_sum = max(max_sum, current_sum)

        return max_sum



        
if __name__ == "__main__":
    sol = Solution()
    nums = [187,470,25,436,538,809,441,167,477,110,275,133,666,345,411,459,490,266,987,965,429,166,809,340,467,318,125,165,809,610,31,585,970,306,42,189,169,743,78,810,70,382,367,490,787,670,476,278,775,673,299,19,893,817,971,458,409,886,434]
    print(sol.maximumUniqueSubarray(nums))