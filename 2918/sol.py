class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        # nums1 = [3,2,0,1,0]
        # nums2 = [6,5,0]
        sum1, sum2 = sum(nums1), sum(nums2)
        nums1Zero = nums1.count(0)
        nums2Zero = nums2.count(0)
        
        if sum1 > sum2:
            bigSum, smallSum = sum1, sum2
            bigZero, smallZero = nums1Zero, nums2Zero
        elif sum2 > sum1:
            bigSum ,smallSum = sum2, sum1
            bigZero, smallZero = nums2Zero, nums1Zero
        else:
            return sum1 + max(nums1Zero, nums2Zero) if (nums1Zero == 0) == (nums2Zero == 0) else -1

        diff = bigSum - smallSum
        # Swap big number's 0 to smaller number
        # Find the mininum of numbers sum(bigSwap) + bigSum = sum(smallSwap) + smallSum
        # sum(swap1) = sum(swap2) - diff
        if smallZero == 0 or diff > smallZero*10**10 - bigZero or diff < smallZero - bigZero*10**10:
            return -1

        return max(bigSum + bigZero, smallSum + smallZero)
