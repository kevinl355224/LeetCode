from typing import List
from collections import Counter

class FindSumPairs:
    """
    1 <= val <= 10**5
    1 <= tot <= 10**9

    1 <= nums1.length <= 1000
    1 <= nums2.length <= 10**5
    """
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.cnt1 = Counter(nums1)
        self.cnt2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        """
        Only update nums2
        """
        origin_val = self.nums2[index]
        new_val = origin_val + val
        self.cnt2[origin_val] -= 1
        self.cnt2[new_val] += 1
        self.nums2[index] = new_val

    def count(self, tot: int) -> int:
        """
        return number of target
        """
        result = 0
        for num1, cnt in self.cnt1.items():
            need = tot - num1
            if need in self.cnt2:
                result += (self.cnt2[need] * cnt)
        return result

            


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)




if __name__ == "__main__":
    commands = ["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"]
    params = [
        [[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]],
        [7],
        [3, 2],
        [8],
        [4],
        [0, 1],
        [1, 1],
        [7]
    ]
    result = []
    for i, cmd in enumerate(commands):
        if cmd == "FindSumPairs":
            nums1, nums2 = params[i]
            find_obj = FindSumPairs(nums1, nums2)
            result.append(None)
        elif cmd == "add":
            index, val = params[i]
            find_obj.add(index, val)
            result.append(None)
        elif cmd == "count":
            tot = params[i][0]
            res = find_obj.count(tot)
            result.append(res)

    print(result)
