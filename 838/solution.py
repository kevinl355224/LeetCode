class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        length = len(dominoes)
        dominoeStatus = [""]*length
        previous_idx = 0
        previous_direction = ""

        for idx in range(length):
            # --->
            # Incoming dominoe is "."
            if dominoes[idx] == ".":
                if previous_direction == "R":
                    # Privious is "R"
                    dominoeStatus[idx] = "R"
                else:
                    # Previous is "L"
                    dominoeStatus[idx] = "."
            # Incoming dominoe is "R"
            elif dominoes[idx] == "R":
                dominoeStatus[idx] = "R"
                previous_direction = "R"
                previous_idx = idx
            # Incoming dominoe is "L", update previous status
            else:
                # update preivious dominoes status
                if previous_direction == "L" or previous_direction == "":
                    dominoeStatus[previous_idx :idx+1] = "L"*(idx-previous_idx+1)

                # previous_direction = "R"
                else:
                    # L...R L..R
                    # 01234 0123 mid = 1.5
                    mid = (idx + previous_idx) / 2
                    # Have mid
                    if mid%1 == 0:
                        mid = int(mid)
                        dominoeStatus[mid] = "."
                        dominoeStatus[mid+1:idx+1] = "L"*(idx-mid)
                    # Don't have mid
                    else:
                        dominoeStatus[int(mid)+1:idx+1] = "L"*(idx - int(mid))
                    previous_direction = "L"

                previous_idx = idx

        ans = "".join(dominoeStatus)
        print(ans)
        return ans

if __name__ == "__main__":
    test = ".L.R...LR..L.."
    sol = Solution()
    print(sol.pushDominoes(test))