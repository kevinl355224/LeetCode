from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # dominoes = [[1,2],[2,1],[3,4],[5,6]]

        # [1,2] = [2,1]
        mapping = {} # {(big, small) : num, ...}
        PairCount = 0
        for dominoe in dominoes:
            if dominoe[0]>dominoe[1]:
                big = dominoe[0]
                small = dominoe[1]
            else:
                big = dominoe[1]
                small = dominoe[0]

            # Search map
            if (big, small) in mapping:
                mapping[(big, small)] += 1
            else:
                mapping[(big, small)] = 1

        for key, val in mapping.items():
            if val > 1:
                print(key, val)
                PairCount += val * (val-1) / 2
        # print(mapping)
        # print(int(PairCount))
        return int(PairCount)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.numEquivDominoPairs(dominoes = [[1,2],[2,1],[3,4],[5,6]]))