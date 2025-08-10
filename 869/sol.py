from collections import Counter
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        """
        Reorder the digits in any order
        The leading digit is not zero
        Return true if and only if we can do this so that the resulting number is a power of two.
        1 <= n <= 10**9
        """
        n_str = str(n)
        digit_cnt = Counter(n_str)
        # Find the min and max range the digits can compose.
        max_edge = 10 ** (len(n_str))
        min_edge = 10 ** (len(n_str) - 1)

        # Find the pow of 2 in this range
        pow_str_list = []
        base = 1
        while base <= max_edge:
            if base >= min_edge:
                pow_str_list.append(str(base))
            base *= 2

        # Check can n_str can compose each num in pow_list
        for pow_str in pow_str_list:
            valid = True
            for key, value in Counter(pow_str).items():
                if digit_cnt[key] != value:
                    valid =False
                    continue
            if valid: return True
            
        return False
    
if __name__ == "__main__":
    sol = Solution()
    n = 8388608
    print(sol.reorderedPowerOf2(n))
