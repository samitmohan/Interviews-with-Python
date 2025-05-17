# https://leetcode.com/problems/bulls-and-cows/

# secret = "1807", guess = "7810"
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        # match
        for i in range(len(secret)):
            bulls += (int)(secret[i] == guess[i])  # 1 (8 matches 8)

        # cows
        for c in set(secret):  # count : occurences in string
            cows += min(
                secret.count(c), guess.count(c)
            )  # will return min count of all same numbers (1 1 1 1 -> 4)
            # subtract this from bulls to get actual cows (4 - 1 : 3)

        # ans
        return str(bulls) + "A" + str(cows - bulls) + "B"  # 1A3B
