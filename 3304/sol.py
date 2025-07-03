class Solution:
    def kthCharacter(self, k: int) -> str:
        """
        Start with letter "a"
        Generate next character in the English alphabet, and append it to the original word.
        Return the value of the kth character in word

        ex. "a" -> "a" + "b", "ab" -> "ab" + "bc"...
        1 <= k <= 500
        """
        pow_2 = [1,]
        while pow_2[-1] < k:
            pow_2.append(pow_2[-1] * 2)
        
        # Find the biggest num in pow_2 smaller than k and substract it
        cnt = 0
        while k != 1:
            for i in range(len(pow_2)):
                if pow_2[i] >= k:
                    k -= pow_2[i - 1]
                    cnt += 1
                    break
        return chr(97 + cnt % 26)


if __name__ == "__main__":
    sol = Solution()
    k = 500
    print(sol.kthCharacter(k))