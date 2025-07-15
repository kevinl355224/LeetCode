import re

class Solution:
    def isValid(self, word: str) -> bool:
        """
        Contains a minimum of 3 characters.
        Only digits (0-9), and English letters (uppercase and lowercase).
        Includes at least one vowel('a', 'e', 'i', 'o', 'u').
        Includes at least one consonant(English letter that is not a vowel).
        """
        
        regex = r"(?i)(?=^.*[b-df-hj-np-tv-z])(?=.*[aieou])^[a-z0-9]{3,}$"
        return re.search(regex, word) is not None
        

if __name__ == "__main__":
    sol = Solution()
    word = "UuE6"
    print(sol.isValid(word))