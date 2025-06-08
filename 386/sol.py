from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        """
        Order in lexicographical.
        [1, 11, 12, 13, ..., 2, 20, 21...]
        """
        result =[]
        curr = 1
        for _ in range(n):
            result.append(curr)
            if curr * 10 <= n:
                curr *= 10
            else:
                # Fill same column tree
                while curr % 10 == 9 or curr + 1 > n:
                    curr //= 10
                curr +=1
        
        # print(result)
        return result

if __name__ == "__main__":
    sol = Solution()
    n = 10
    print(sol.lexicalOrder(n))
