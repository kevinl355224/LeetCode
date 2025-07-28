from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        """
        Return the number of different non-empty subsets with the maximum bitwise OR.
        The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).
        1 <= nums.length <= 16
        1 <= nums[i] <= 10**5
        """
        # Caculate the max bitewise OR
        max_or = 0
        self.cnt = 0

        for num in nums:
            max_or |= num

        def dfs(index, current_or):
            if index == len(nums): 
                if current_or == max_or:
                    self.cnt += 1
                return
            # Skip num
            dfs(index + 1, current_or)
            # Select num
            dfs(index + 1, current_or | nums[index])

        dfs(0, 0)

        return self.cnt

if __name__ == "__main__":
    sol = Solution()
    nums = [3,1]
    print(sol.countMaxOrSubsets(nums))