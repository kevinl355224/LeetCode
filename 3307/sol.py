from typing import List

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        """
        Start with letter "a"
        
        Return the value of the kth character in word after performing all the operations.

        operations[i] = 0
        Append a copy of word to itself.
        ex. "a" -> "a" + "a", "ab" -> "ab" + "ab"...
        
        operations[i] = 1
        Generate next character in the English alphabet, and append it to the original word.
        ex. "a" -> "a" + "b", "ab" -> "ab" + "bc"...

        1 <= k <= 10**14
        1 <= operations.length <= 100
        """
        


        return chr(ord("a") + ((k - 1) & int("".join(str(x) for x in operations[::-1]), 2)).bit_count() % 26)


if __name__ == "__main__":
    sol = Solution()
    k = 5
    operations = [0,0,0]
    print(sol.kthCharacter(k, operations))