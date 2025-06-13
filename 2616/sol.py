from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        """
        Try find little difference

        1 <= nums.length <= 10**5
        0 <= nums[i] <= 10**9

        If p pairs can be formed with a maximum difference of D(max_diff),
        then they can also be formed with any difference greater than D.
        """
        nums.sort()
        length = len(nums)
        
        def isValid(max_diff):
            # Linear scan through nums
            idx, cnt = 0, 0
            while idx < length - 1:
                if nums[idx + 1] - nums[idx] <= max_diff:
                    cnt += 1
                    idx += 2
                    if cnt == p:
                        return True
                else:
                    idx += 1
            return False

        if p == 0 : return 0
                
        # Binary tree for diffenence
        # left is 0 diff
        # Right is max diff in current nums
        left, right = 0, nums[-1] - nums[0]
        while left <= right:
            mid = (left + right) // 2
            # max_diff = left + (right - left) // 2 # Python won't overflow
            if isValid(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
            
if __name__ == "__main__":
    sol = Solution()
    nums = [10,1,2,7,1,3]
    p = 2
    print(sol.minimizeMax(nums, p))