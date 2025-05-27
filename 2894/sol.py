class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        """
        n = 10, m = 3
        [1, 10] that are not divisible by 3 are [1,2,4,5,7,8,10] sum = 37
        [1, 10] that are divisible by 3 are [3,6,9] sum = 18
        return 37 - 18

        1 <= n, m <= 1000
        
        ans = num1 - num2
        total = n(n+1)/2
        num1 = total - divisible_sum
        num2 = divisible_sum

        divisible_sum = m + 2m + 3m +...+ km = m(1+2+3+...+k)
                        = m(k(k+1))/2
        k = n // m 
        divisible_sum = m*(n//m)*(n//m+1)/2

        ans = total - 2*divisible_sum
            = n*(n+1)/2 - 2*m*(n//m)*(n//m+1)/2
            
        Because return interger so /2 -> //2
        """
        return n*(n+1)//2 - m*(n//m)*(n//m+1)


if __name__ == "__main__":
    sol = Solution()
    m = 1
    n = 5
    print(sol.differenceOfSums(m=m, n=n))