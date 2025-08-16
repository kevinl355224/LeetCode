class Solution:
    def maximum69Number (self, num: int) -> int:
        """
        Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
        1 <= num <= 10**4
        """
        for i, digit in enumerate(str(num)):
            if digit == "6":
                return num + 3 * 10 ** (len(str(num)) - i - 1)
        return  num

if __name__ == "__main__":
    sol = Solution()
    num = 9999

    print(sol.maximum69Number(num))