from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        """
        len(nums) // 3 = 0
        Divide the array nums into n / 3 arrays of size 3.
        The difference between any two elements in one array is less than or equal to k
        Return a 2D array containing the arrays. If it is impossible to satisfy the conditions, return an empty array. 
        And if there are multiple answers, return any of them.
        
        nums = [1,3,4,8,7,9,3,5,1] k =2
        Output: [[1,1,3],[3,4,5],[7,8,9]]

        1 <= n <= 10**5
        """
        # Sort the numbers
        nums.sort()
        result = []

        for i in range(0, len(nums), 3):
            if nums[i+2] - nums[i] > k:
                return []
            result.append(nums[i:i+3])

        return result


if __name__ == "__main__":
    sol = Solution()
    nums = [1,3,4,8,7,9,3,5,1]
    k = 2
    print(sol.divideArray(nums, k))