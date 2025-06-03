from typing import List
from collections import deque

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        """
        n == status.length == candies.length == keys.length == containedBoxes.length
        1 <= n <= 1000
        """
        q = deque()
        owned_keys = set()
        owned_locked_boxes = set()
        total = 0

        # Process initial boxes
        for box in initialBoxes:
            if status[box]:
                q.append(box)
            else:
                owned_locked_boxes.add(box)

        while q:
            # Open boxes
            box = q.popleft()
            new_boxes = containedBoxes[box]
            new_keys = keys[box]
            total += candies[box]

            # Check and distribute new_boxes
            for new_box in new_boxes:
                if status[new_box] or new_box in owned_keys:
                    q.append(new_box)
                else:
                    owned_locked_boxes.add(new_box)

            # Check new_keys
            for new_key in new_keys:
                if new_key in owned_locked_boxes:
                    owned_locked_boxes.remove(new_key)
                    q.append(new_key)
                owned_keys.add(new_key)

        return total


if __name__ == "__main__":

    status = [1,0,1,0]
    candies = [7,5,4,100]
    keys = [[],[],[],[]]
    containedBoxes = [[1,2],[3],[],[]]
    initialBoxes = [1,2]
    sol = Solution()
    print(sol.maxCandies(status, candies, keys, containedBoxes, initialBoxes))