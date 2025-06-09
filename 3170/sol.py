from collections import Counter
from heapq import heapify
import bisect

class Solution:
    def clearStars(self, s: str) -> str:
        """
        Return the lexicographically smallest resulting string after removing all '*' characters.
        1 <= s.length <= 10**5

        # Try to remove the closest small non-"*" character.
        """
        num_star = s.count("*")
        seq = [] # Save the closet small non [[letter, -idx], []]

        remove_set = set()

        # print(word_list)
        for idx, letter in enumerate(s):
            if letter == "*":
                # Remove the smallest non="*" in seq
                word, idx = seq.pop(0)
                remove_set.add(-idx)
            else:
                # Add num into 
                if len(seq) < num_star:
                    bisect.insort(seq, [letter, -idx])
                else:
                    # Add seq
                    bisect.insort(seq, [letter, -idx])
                    seq.pop() # remove last one

        # print(remove_set)
        # Reverse del
        filtered_list = [x for idx, x in enumerate(s) if idx not in remove_set and x != "*"]
        return "".join(filtered_list)
        
if __name__ == "__main__":
    sol = Solution()
    s = "aababbbb**"
    print(sol.clearStars(s))
