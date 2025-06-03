from typing import List
from collections import deque

class Solution:
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        q = deque()
        owned_keys = set()
        owned_locked_boxes = set()
        visited = set()
        total = 0

        for box in initialBoxes:
            if status[box]:
                q.append(box)
            else:
                owned_locked_boxes.add(box)

        while q:
            box = q.popleft()
            if box in visited:
                continue
            visited.add(box)

            total += candies[box]

            # process keys
            for key in keys[box]:
                if key not in owned_keys:
                    owned_keys.add(key)
                    if key in owned_locked_boxes:
                        owned_locked_boxes.remove(key)
                        q.append(key)

            # process contained boxes
            for new_box in containedBoxes[box]:
                if status[new_box] or new_box in owned_keys:
                    q.append(new_box)
                else:
                    owned_locked_boxes.add(new_box)

        return total


if __name__ == "__main__":

    status = [1,0,1,0]
    candies = [7,5,4,100]
    keys = [[],[],[],[]]
    containedBoxes = [[1,2],[3],[],[]]
    initialBoxes = [1,2]
    sol = Solution()
    print(sol.maxCandies(status, candies, keys, containedBoxes, initialBoxes))