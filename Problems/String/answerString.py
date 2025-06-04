# https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/
# Good Question 

def answerString(word: str, numFriends: int) -> str:
    if numFriends == 1:
        return word
    biggest_word = ""
    n = len(word) - numFriends + 1
    for i in range(len(word)):
        biggest_word = max(word[i : i + n], biggest_word)
    return biggest_word


def main():
    print(answerString(word="aann", numFriends=2)) # nn is better than ann

main()

