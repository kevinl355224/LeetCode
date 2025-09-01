from typing import List
import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        heapq.heapify(heap)

        def cal_new_ratio(passed, total):
            return (passed + 1) / (total + 1) - passed/total  

        for passed, total in classes:
            ratio = cal_new_ratio(passed, total)
            heapq.heappush(heap, (-ratio, passed, total))
            
        while extraStudents > 0:
            _, passed, total = heapq.heappop(heap)
            passed += 1
            total += 1
            new_delta = cal_new_ratio(passed, total)
            heapq.heappush(heap, (-new_delta, passed, total))
            extraStudents -= 1

        average = 0
        for _, passed, total in heap:
            average += passed / total
        return average / len(heap)



if __name__ == "__main__":
    sol = Solution()
    classes = [[1,2],[3,5],[2,2]]
    extraStudents = 2
    print(sol.maxAverageRatio(classes, extraStudents))