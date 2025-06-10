from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        """
        maximum difference diff = a1 - a2
        a1 has an odd frequency in the string.
        a2 has an even frequency in the string.

        Find max a1 and min a2
        """
        max_odd, min_even = 0, float("inf")
        count = Counter(s)
        for _, value in count.items():
            if value & 1:
                max_odd = max(max_odd, value)
            else:
                min_even = min(min_even, value)
        return max_odd - min_even

if __name__ == "__main__":
    sol = Solution()
    s = "aaaaabbc"
    print(sol.maxDifference(s))