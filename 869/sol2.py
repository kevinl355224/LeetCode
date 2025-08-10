class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        """
        Reorder the digits in any order
        The leading digit is not zero
        Return true if and only if we can do this so that the resulting number is a power of two.
        1 <= n <= 10**9
        """
        def sorted_digits(num):
            """
            Count and order the num
            ex. 8388608 -> "0368888"
            """
            return "".join(sorted(str(num)))
        
        target = sorted_digits(n)

        for i in range(31):
            if sorted_digits(1 << i) == target:
                return True
        return False

if __name__ == "__main__":
    sol = Solution()
    n = 8388608
    print(sol.reorderedPowerOf2(n))
