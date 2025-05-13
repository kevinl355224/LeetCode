class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        # s = "jajsda"
        # Counter(s) = Counter({'j': 2, 'a': 2, 's': 1, 'd': 1})
        # *ascii_lowercase = a,b,c...,z
        # itemgetter(*ascii_lowercase) : get all lowercase item value to tuple
        # = (2, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0)
        # 
        q = deque(itemgetter(*ascii_lowercase)(Counter(s)))
        for _ in range(t):
            q.appendleft(q.pop()) # Get last z to first position, then all move right to next word.
            q[1] += q[0] # If the original q[25] is n, meaning there are n occurrences of "z", 
                         # then after rotating it to position q[0], we add n to "b" at q[1].
        return sum(q)%(10**9+7)

if __name__ == "__main__":
    sol = Solution()
    s = "abcyy"
    t = 100
    print(sol.lengthAfterTransformations(s=s, t=t))