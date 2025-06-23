class Solution:
    def kMirror(self, k: int, n: int) -> int:
        """
        Given the base k and the number n, return the sum of the n smallest k-mirror numbers.
        1 <= n <= 30
        2 <= k <= 9
        
        base-x : 0000101 <--
        """
        ans = 0
        cnt = 0

        def create_palindrome(num, odd):
            """
            Use to create 10-base palindrome
            num = 12345
            """
            x = num
            if odd:
                # If odd = True → x // 10 = 1234
                x //= 10
            while x > 0:
                # Put the last num in x to num
                num = num * 10 + x % 10
                x //= 10
            return num

        def is_palindrome(num, base):
            """
            Put each num into list
            num = 123 → digit_list = [1, 2, 3]
            """
            digit_list = []
            while num > 0:
                digit_list.append(num % base)
                num //= base
            return digit_list == digit_list[::-1]

        total = 0
        cnt = 0
        length = 1 # Control the current number of digits to generate
        
        while cnt < n:
            # Create odd palindrome
            # 12 -> 121
            for i in range(length, length * 10):
                if cnt >= n:
                    break
                result = create_palindrome(i, True)
                if is_palindrome(result, k):
                    total += result
                    cnt += 1
            # Create even palindrome
            # 12 -> 1221
            for i in range(length, length * 10):
                if cnt >= n:
                    break
                result = create_palindrome(i, False)
                if is_palindrome(result, k):
                    total += result
                    cnt += 1

            length *= 10
        return total
    
if __name__ == "__main__":
    sol = Solution()
    k = 3
    n = 7
    print(sol.kMirror(k, n))