from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        """
        We consider word to be k-special 
        if |freq(word[i]) - freq(word[j])| <= k for all indices i and j in the string.

        Return the minimum number of characters you need to delete to make word k-special.

        1 <= word.length <= 10**5
        """
        cnt = Counter(word)
        min_deletion = float("inf")
        visited = set()
        freq_list = sorted(cnt.values())

        # Try each frequency as the base
        for i in range(len(freq_list)):
            if freq_list[i] in visited:
                continue
            visited.add(freq_list[i])
            base = freq_list[i]
            deletion_cnt = 0
            # Delete the nums < base
            for num in freq_list[:i]:
                deletion_cnt += num

            # Delete the nums > base + k
            for num in freq_list[i+1:]:
                if num > base + k:
                    deletion_cnt += num - base - k
            
            min_deletion = min(min_deletion, deletion_cnt)

        return min_deletion

if __name__ == "__main__":
    sol = Solution()
    word = "aabcaba"
    k = 0
    print(sol.minimumDeletions(word, k))
