class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        i = 1

        def count(curr):
            result = 0
            nei = curr + 1

            while curr <= n:
                nei = min(n+1, nei)
                result += nei - curr
                curr *= 10
                nei *= 10
            return result

        while i < k:
            steps = count(curr)
            if i + steps <= k:
                # Move to next
                # 1 -> 2
                curr += 1
                i += steps
            else:
                # Move down
                # 1 -> 10 ~ 19
                curr *= 10
                i += 1
        return curr

if __name__ == "__main__":
    sol = Solution()
    n = 2
    k = 2
    print(sol.findKthNumber(n, k))
