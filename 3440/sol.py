from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        """
        Can reschedule at most one meeting by moving its start time while maintaining the same duration.
        Return the maximum amount of free time possible after rearranging the meetings.

        It is valid for the relative ordering of the meetings to change after rescheduling one meeting.

        1 <= eventTime <= 10**9
        n == startTime.length == endTime.length
        2 <= n <= 10**5
        """

        vacancy_list = []
        # Scan all time
        current = 0
        for idx, (start, end) in enumerate(zip(startTime, endTime)):
            vacancy_list.append((start - current, idx))
            current = end        

        vacancy_list.append((eventTime - current, len(startTime)))
        # Only focus on 4 lagest vacancy
        lagest_4_vacancy = sorted(vacancy_list)[-4:]
        
        # print(vacancy_list)
        # print(lagest_4_vacancy)

        max_vacancy = 0
        for idx in range(len(vacancy_list)-1):
            interval = endTime[idx] - startTime[idx]

            is_insert_available = False
            for vacancy, insert_idx_loc in lagest_4_vacancy:
                # [1, 0] means current vacancy is nearby current event.
                if vacancy >= interval and insert_idx_loc-idx not in [1, 0]:
                    is_insert_available = True
                    break
            # If only move event to left or right
            sub_free_time = vacancy_list[idx][0] + vacancy_list[idx+1][0]

            if is_insert_available:
                sub_free_time += interval
            max_vacancy = max(max_vacancy, sub_free_time)

        return max_vacancy

if __name__ == "__main__":
    sol = Solution()
    eventTime = 5
    startTime = [1,3]
    endTime = [2,5]
    print(sol.maxFreeTime(eventTime, startTime, endTime))