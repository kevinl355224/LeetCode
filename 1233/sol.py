from typing import List
from collections import deque
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        """
        Given a list of folders folder, 
        return the folders after removing all sub-folders in those folders. 
        You may return the answer in any order.

        1 <= folder.length <= 4 * 10**4
        2 <= folder[i].length <= 100
        Each folder name is unique.
        """
        # Only compare the previous folder after sort
        folder.sort()
        result = [folder[0]]
        for i in range(1, len(folder)):
            pre = result[-1] + "/"
            if not folder[i].startswith(pre):
                result.append(folder[i])
        return result

if __name__ == "__main__":
    sol = Solution()
    folder = ["/a","/xc/ee","/a/b","/c/d","/c/d/e","/c/f"]
    print(sol.removeSubfolders(folder))
