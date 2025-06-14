class Solution:
    def minMaxDifference(self, num: int) -> int:
        """
        num = 11891
        remap the digit 1 to the digit 9, max = 99899
        remap the digit 1 to the digit 0, min = 890

        diff = 99009
        The diff only in remap num
        1 <= num <= 10**8
        
        Convert the first 0-8 to 9.
        Convert the first 1-9 to 0.
        """

        d1, d2 = "9", "0"
        num_str = str(num)
        # Get d1, d2
        for n in num_str:
            if n != "9":
                d1 = n
                break

        for n in num_str:
            if n != "0":
                d2 = n
                break

        num1 = int(num_str.replace(d1, "9"))
        num2 = int(num_str.replace(d2, "0"))

        return num1 - num2

if __name__ == "__main__":
    sol = Solution()
    num = 99999
    print(sol.minMaxDifference(num))