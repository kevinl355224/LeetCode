from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # dominoes = [[1,2],[2,1],[3,4],[5,6]]

        mapping = [0]*100 # [ 12:num, 23:num... ]
        PairCount = 0
        for dominoe  in dominoes:
            if dominoe[0]>dominoe[1]:
                x = 10*dominoe[0] + dominoe[1] 
            else:
                x = 10*dominoe[1] + dominoe[0] 
            
            PairCount += mapping[x]
            mapping[x] += 1

        # print(mapping)
        # print(PairCount)
        return PairCount


if __name__ == "__main__":
    sol = Solution()
    print(sol.numEquivDominoPairs(dominoes = [[1,2],[2,1],[3,4],[5,6]]))