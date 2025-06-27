from collections import deque, Counter

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        """
        Find the longest subsequence repeated k times in string s.

        2 <= s.length, k <= 2000
        """
        if k == 1: return s
        cnt = Counter(s)
        # Only use the letter which reapeted >= k times
        alphabet = [ch for ch in sorted(cnt, reverse=True) if cnt[ch] >= k]
        q = deque() # ["xe", "cd"]
        q.append("")
        longest_sub = ""

        def get_repeated_times(sub_s: str) -> int:
            cnt = 0
            lenght = len(sub_s)
            index = 0
            for letter in s:
                if letter == sub_s[index]:
                    index += 1
                    if index == lenght:
                        cnt += 1
                        index = 0
            return cnt

        # bfs
        while q:
            sub_s = q.popleft()
            for letter in alphabet:
                new_s = sub_s + letter
                if len(new_s) * k > len(s):
                    continue

                if get_repeated_times(new_s) >= k:
                    q.append(new_s)
                    if len(new_s) > len(longest_sub) or (len(new_s) == len(longest_sub) and new_s > longest_sub):
                        longest_sub = new_s

        return longest_sub



if __name__ == "__main__":
    sol = Solution()
    s = "kkrkmktkkhqdlkzqfdmkkghjk"
    k = 9
    print(sol.longestSubsequenceRepeatedK(s, k))