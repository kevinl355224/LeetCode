from collections import Counter

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        """
        maximum difference if substring
        a1 has an odd frequency in the substring.
        a2 has an even frequency in the substring.

        subs has a size of at least k.
        Find all substring >= k
        
        Find max a1 and min a2 in the substring
        diff = a1 - a2

        s consists only of digits '0' to '4'.
        3 <= s.length <= 3 * 10**4
        """
        
        count = Counter(s)
        max_diff = -float("inf")

        def count_diff(count):
            max_odd, min_even = -float("inf"), float("inf")
            for _, value in count.items():
                # print(_, " ", value)
                if value > 0:
                    if value & 1:
                        max_odd = max(max_odd, value)
                    else:
                        min_even = min(min_even, value)
            return max_odd - min_even

        max_len = len(s)
        for lenght in range(k, max_len+1):
            left = 0
            right = lenght
            # Count initial stat
            count = Counter(s[:lenght])
            max_diff = max(count_diff(count), max_diff)
            for step in range(max_len-lenght):
                # Window sliding forward
                # Cut left
                count[s[left + step]] -= 1
                # Add right
                count[s[right + step]] += 1
                # Count diff
                max_diff = max(count_diff(count), max_diff)

        return max_diff

if __name__ == "__main__":
    sol = Solution()
    s = "2222130"
    k = 3
    print("ans:", sol.maxDifference(s, k))