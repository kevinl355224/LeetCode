from typing import List

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # nums = [3,3,3]
        # equilateral, isosceles, scalene or none
        # If on of nums[i]+nums[j] > nums[k] can't form a triangle
        nums.sort()
        
        # Check triangle inequality
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        
        a, b, c = nums
        if a == c:
            return "equilateral"
        elif a == b or b == c:
            return "isosceles"
        else:
            return "scalene"
        
if __name__ == "__main__":
    sol = Solution()
    nums = [3,3,3]
    print(sol.triangleType(nums))