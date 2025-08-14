class Solution:
    def largestGoodInteger(self, num: str) -> str:
        """
        good string : len(substring) = 3, consists of only one unique digit.
        Return the maximum good integer as a string or an empty string "" if no such integer exists.
        3 <= num.length <= 1000
        """
        max_result = "-1"
        
        for i in range(2, len(num)):
            if num[i] == num[i - 1] and num[i] == num[i - 2]:
                max_result = max(max_result, num[i])
                if max_result == "9":
                    break
        return max_result * 3 if max_result != "-1" else ""

if __name__ == "__main__":
    sol = Solution()
    num = "677713333999"
    print(sol.largestGoodInteger(num))