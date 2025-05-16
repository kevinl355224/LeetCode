import heapq
from typing import List

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        # words = ["bab","dab","cab"]
        # groups = [1,2,2]
        # group[i] != group[i-1]
        # len(words[i]) == len(words[i-1])
        # hamming distance between them is 1

        # 1 <= n == words.length == groups.length <= 1000
        # 1 <= words[i].length <= 10

        # Find Possible longest connection for each words
        queue = [[-1, 0, -1]] # [negitive length, idx of word, parent]
        heapq.heapify(queue)

        memo = {i: -1 for i in range(len(words))} # words_idx : longest path parent idx, -1 meaning no parent

        def hamming_dist(a,b):
            return sum(x != y for x,y in zip(a,b))
        

        for i in range(1, len(words)):
            temp_q = []
            while queue:
                length, idx, parent = heapq.heappop(queue)
                temp_q.append((length, idx, parent))
                # Check 
                if len(words[i]) == len(words[idx]) and groups[i] != groups[idx] and hamming_dist(words[i], words[idx]) == 1:
                    memo[i] = idx
                    heapq.heappush(queue, (length-1, i, idx))
                    break
            # Can't find a parent
            if not queue:
                heapq.heappush(queue, (-1, i, -1))

            # Recover queue
            for data in temp_q:
                heapq.heappush(queue, data)
        
        # print("Queue:", queue)
        # print("Memo:", memo)
        # Get path
        length, idx, parent = heapq.heappop(queue)
        length = -length
        path = [""]*(length)

        for i in reversed(range(length)):
            path[i] = words[idx]
            idx = memo[idx]

        return path

if __name__ == "__main__":
    words = ["bdb","aaa","ada"]
    groups = [2,1,3]
    sol = Solution()
    print(sol.getWordsInLongestSubsequence(words, groups))
