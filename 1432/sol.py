class Solution:
    def maxDiff(self, num: int) -> int:
        """
        num = 555
        1. pick x = 5, y = 9 → a = 999
        2. pick x = 5, y = 1 → a = 111
        Diff = 888
        Return the max difference between a and b.

        1 <= num <= 10**8
        Note that neither a nor b may have any leading zeros, and must not be 0.
        """
        num_str = str(num)

        for n in num_str:
            if n != "9":
                max_num = int(num_str.replace(n, "9"))
                break
        else:
            max_num = num

        # If num start from 1. Convert the second non-1 number to 0.
        if num_str[0] == "1":
            for n in num_str:
                if n not in ["1", "0"]:
                    min_num = int(num_str.replace(n, "0"))
                    break
            else:
                min_num = num
        # If num start from 2-9. Convert the first num to 1.
        else:
            min_num = int(num_str.replace(num_str[0], "1"))
        # print(max_num, min_num)
        return max_num - min_num

if __name__ == "__main__":
    sol = Solution()
    num = 9288
    print(sol.maxDiff(num))
