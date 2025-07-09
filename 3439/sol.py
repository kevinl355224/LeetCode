from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        """
        move the section to vacant the bigest space

        The relative order of all the event should stay the same and they should remain non-overlapping.
        
        1 <= eventTime <= 10**9
        n == startTime.length == endTime.length
        2 <= n <= 10**5
        """
        vacancy_list = [] # save 
        current_time = 0

        # Scan all event
        for start, end in zip(startTime, endTime):
            vacancy_list.append(start - current_time)
            current_time = end
        
        vacancy_list.append(eventTime - current_time)

        # Find the longest part
        # Use sliding window
        window_size = k + 1
        current_val = sum(vacancy_list[:window_size])
        max_vacancy = current_val
        
        for idx in range(len(vacancy_list) - (k + 1)):
            current_val += - vacancy_list[idx] + vacancy_list[idx + k + 1]
            
            max_vacancy = max(max_vacancy, current_val)
        return max_vacancy

if __name__ == "__main__":
    sol = Solution()
    eventTime = 10
    k = 1
    startTime = [0,2,9]
    endTime = [1,4,10]

    print(sol.maxFreeTime(eventTime, k, startTime, endTime))