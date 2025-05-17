# . would match any character : tricky part
# word may contain dots '.' where dots can be matched with any letter.
# to solve the . : dfs on all nodes : see example (bad = .ad)
# https://leetcode.com/problems/design-add-and-search-words-data-structure/
# Explanation : https://www.youtube.com/watch?v=BTf05gs_8iU


class TrieNode:
    def __init__(self) -> None:
        self.children = {}  # can have 26 children :: # a : TrieNode
        self.end_of_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if not char in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]  # if it does exist, shift curr pointer to it
        curr.end_of_word = True

    # search character can be a "." also : going down 26 different paths (recursive DFS)
    def search(self, word: str) -> bool:
        def dfs(j, root):  # index and current node we're at
            curr = root

            for i in range(j, len(word)):
                char = word[i]
                if char == ".":
                    for child in curr.children.values():  # hashmap values : children
                        if dfs(
                            i + 1, child
                        ):  # if next found .ab : a and b found : return True
                            return True
                    return False
                else:  # normal character
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            return curr.end_of_word  # true or false

        return dfs(0, self.root)
