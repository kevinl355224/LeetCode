from typing import List

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        """
        If trainer[j] > players[i] than match.

        1 <= players.length, trainers.length <= 10**5
        1 <= players[i], trainers[j] <= 10**9
        """
        cnt = 0
        players.sort(reverse=True)
        trainers.sort(reverse=True)
        p_idx = 0
        t_idx = 0
        while p_idx < len(players) and t_idx < len(trainers):
            if players[p_idx] <= trainers[t_idx]:
                p_idx += 1
                t_idx += 1
                cnt += 1
            else:
                p_idx += 1
            
        return cnt


if __name__ == "__main__":
    sol = Solution()
    players = [4,7,9]
    trainers = [8,2,5,8]
    print(sol.matchPlayersAndTrainers(players, trainers))
