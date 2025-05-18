from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [2,0,2,1,1,0] -> [0,0,1,1,2,2]
        # Sorting 0, 1, 2

        # n == nums.length
        # 1 <= n <= 300
        front = 0
        mid = 0
        end = len(nums)-1
        while mid <= end:
            if nums[mid] == 0:
                nums[front], nums[mid] = nums[mid], nums[front]
                front += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[end] = nums[end], nums[mid]
                end -= 1
