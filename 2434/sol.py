from collections import deque, Counter

class Solution:
    def robotWithString(self, s: str) -> str:
        """
        s = "zza"
        Return "azz"
        1 <= s.length <= 10**5
        s.pop(0) ➜ t.append()
        t.pop() ➜ p.append()

        a -> z
        """
        n = len(s)
        minidx = [-1]*n
        min_ = s[-1]
        minidx[-1] = idx = n-1 # init last word
        for i in range(n-2, -1, -1): # Start with Second-last
            if s[i] <= min_:
                min_ = s[i]
                idx = i
            minidx[i] = idx
        
        # print(f"minidx:{minidx}")

        p = []
        t = []
        idx_pre = -1
        idx = minidx[0]
        while t or idx < n:
            if not t or (idx < n and t[-1] > s[idx]):
                p.append(s[idx])
                t += [c for c in s[idx_pre + 1: idx]]
                idx_pre = idx
                idx = minidx[idx + 1] if idx + 1 < n else n
            else:
                p.append(t.pop())
            # print(f"t:{t} idx:{idx} P:{P}")
        p += t[::-1]
        return "".join(p)
    
if __name__ == "__main__":
    sol = Solution()
    s = "bzcbb"
    print(sol.robotWithString(s))