class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        """
        1 <= s1.length, s2.length, baseStr <= 1000
        """
        length = len(s1)

        # To skip the pair which is processed.
        processed_pair = set()

        # If processed both word in processed letter, combine two group.
        group = [] # [{word, word}, ]
        word_map = {} # word : group number
        idx = 0

        # Put equalence word in a set
        for i in range(length):
            pair = tuple(sorted((s1[i], s2[i])))
            if pair in processed_pair:
                continue
            # Add pair to processed_pair
            processed_pair.add(pair)
            letter_1 = s1[i]
            letter_2 = s2[i]

            if letter_1 in word_map and letter_2 in word_map:
                # Combine group 2 to 1.
                group_1_idx = word_map[letter_1]
                group_2 = group[word_map[letter_2]]
                group[group_1_idx] = group[group_1_idx] | group_2
                # Update word map
                for word in group_2:
                    word_map[word] = group_1_idx

            elif letter_1 in word_map:
                # Put letter_2 in letter_1 group
                group_idx = word_map[letter_1]
                word_map[letter_2] = group_idx
                group[group_idx].add(letter_2)

            elif letter_2 in word_map:
                group_idx = word_map[letter_2]
                word_map[letter_1] = group_idx
                group[group_idx].add(letter_1)
            else:
                # Create a new group
                group.append(set([letter_1, letter_2]))
                # Update word_map
                word_map[letter_1] = idx
                word_map[letter_2] = idx
                idx += 1

        # Transfer baseStr
        result = ""
        for letter in baseStr:
            result += min(group[word_map[letter]]) if letter in word_map else letter
        return result

if __name__ == "__main__":
    sol = Solution()
    s1 = "parker"
    s2 = "morris"
    baseStr = "parser"    
    print(sol.smallestEquivalentString(s1, s2, baseStr))