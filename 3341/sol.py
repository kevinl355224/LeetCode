from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # [[0,4,5],[4,4,5],[5,5,5]]
        #               m(j)
        #   start -> 0  4  5
        #       n(i) 4  4  5 
        #            5  5  5 <- goal
        # 1 sec / move
        # Use a array[n*m] records the minimum time to reach.
        m = len(moveTime[0])
        n = len(moveTime)
        minArray = [[-1]*m for _ in range(n)]
        print(moveTime)
        print(f"n: {n}, m: {m}, minArray: {minArray}\n")

        def updateAdjacent(i, j, times):
            # print(f"\ni: {i}, j: {j}, times: {times}")
            minArray[i][j] = times 
            # print(minArray)
            # Move right if not reach the border
            if j+1 < m:
                step = max(times, moveTime[i][j+1]) + 1
                # The next point hasn't been assigned a value yet.
                if minArray[i][j+1] == -1:
                    updateAdjacent(i, j+1, step)
                # Find a better route
                elif minArray[i][j+1] > step:
                    updateAdjacent(i, j+1, step)

            # move down
            if i+1 < n:
                step = max(times, moveTime[i+1][j]) + 1
                if minArray[i+1][j] == -1:
                    updateAdjacent(i+1, j, step)
                elif minArray[i+1][j] > step:
                    updateAdjacent(i+1, j, step)

            # move left
            if j-1 >= 0:
                step = max(times, moveTime[i][j-1]) + 1
                if minArray[i][j-1] == -1:
                    updateAdjacent(i, j-1, step)
                elif minArray[i][j-1] > step:
                    updateAdjacent(i, j-1, step)

            # move up
            if i-1 >= 0:
                step = max(times, moveTime[i-1][j]) + 1
                if minArray[i-1][j] == -1:
                    updateAdjacent(i-1, j, step)
                elif minArray[i-1][j] > step:
                    updateAdjacent(i-1, j, step)

        updateAdjacent(0,0,0)
        print(minArray)
        print(minArray[n-1][m-1])
        
        return minArray[n-1][m-1]

if __name__ == "__main__":
    sol = Solution()
    test = [[0,635144403,259626676,185959080,626238293,586486184,78516406,252708069,701983324,446596001,9292774,14264838,64435474,947607052,875105648,232979285,268935567,642957779,334074470,780277670],[477172392,912542224,736342196,385164416,863994225,618130272,756608968,190079273,507433468,776528015,643560370,364997654,299997797,997069266,234645198,665537344,343659797,174636978,791500965,147327466],[118069212,28631098,204371217,678519721,897811037,156224968,479765378,10545707,553349503,575802145,352915483,598341819,60931541,863797691,367260721,362762707,882393838,633718317,332057911,760073777],[213130052,885461387,824984553,715887013,984800387,744039913,549215577,294887059,943432788,332042592,126749165,742072054,499781496,429563751,762956303,24361520,299153911,370020123,117240131,618727988],[684899204,203913597,539056178,166830462,978722082,230942993,480604211,891213170,789765560,620688232,106074736,482269404,258063633,28316439,607660213,57283828,377425198,899102578,644690094,0]]
    print(sol.minTimeToReach(moveTime=test))