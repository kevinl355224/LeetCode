MOD = 10**9 + 7

# Quick Power
def qpow(base, exp):
    result = 1
    while exp != 0:
        if exp & 1:
            result = (result * base) % MOD
        base = base * base % MOD
        exp >>= 1
    return result

def mod_inv(denominator):
    # Fermat's little theorem
    # x**(p−1) ≡ 1 (mod p)
    # x**(-1) ≡ x**(p-2) (mod p)
    return qpow(denominator, MOD - 2)

# Comb
def comb(n, k):
    if k < 0 or k > n:
        return 0
    numerator = 1
    denominator = 1

    for i in range(k):
        # numerator = n(n-1)(n-2)...
        # denominator = k(k-1)(k-2)...
        numerator = (numerator * (n - i)) % MOD
        denominator = (denominator * (i + 1)) % MOD
    return (numerator * mod_inv(denominator)) % MOD

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        """
        Good array:
        1. len(arr) = n
        2. Element in arr is in the inclusive range [1, m]
        3. k indices i arr[i-1] == arr[i]

        Return the number of good arrays that can be formed.
        Since the answer may be very large, return it modulo 10**9 + 7.

        1 <= n <= 10**5
        1 <= m <= 10**5
        0 <= k <= n - 1
        """
  
        if n == 1:
            return m if k == 0 else 0
        
        """
        Step 1.
        If n = 7, k = 3
        [*, *, *, *, *, *, *]
        There has (n-1) gap in array.
        And k number is equal to the left. Meaning k gaps left is equal right.
        """
        ways_to_choose_k_pairs =  comb(n - 1, k)

        """
        Step 2.
        There are (n - k) sections.
        The first num could choose from [1 ,m].
        Cause each section can't have same number as left. Only (m - 1) could choose.
        """
        ways_to_assign_values = m * qpow(m-1, n - k - 1) % MOD

        return ways_to_choose_k_pairs * ways_to_assign_values % MOD


if __name__ == "__main__":
    sol = Solution()
    n = 3
    m = 2
    k = 1
    print(sol.countGoodArrays(n, m, k))