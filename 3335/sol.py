class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        # z -> ab
        # a -> b -> c ...
        # chr("a") = 97, chr("z") = 123
        # Normalize a=0, b=1, c=3...z=25
        # count(n) = count(n-26) + count(n-25)
        # return length

        MOD = 10**9 +7
        arr = [ord(c)-97+t for c in s]
        ans=0
        memo = {}
        def count(n):
            if n < 26:
                return 1
            if n in memo:
                return memo[n]
            result = count(n-26) + count(n-25)  
            memo[n] = result
            return memo[n]

        for n in arr:
            ans = (ans + count(n))%MOD
        
        return ans

if __name__ == "__main__":
    sol = Solution()
    s = "abcyy"
    t = 100
    print(sol.lengthAfterTransformations(s=s, t=t))