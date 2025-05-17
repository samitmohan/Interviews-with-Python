# https://leetcode.com/problems/implement-trie-prefix-tree/
# https://medium.com/basecs/trying-to-understand-tries-3ec6bede0014


class TrieNode:
    def __init__(self) -> None:
        self.children = {}  # can have 26 children
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()  # empty Tree

    def insert(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()  # empty trie node with char
            curr = curr.children[char]  # if already exist, curr sets to that child
        # apple created. curr is set to e (end_of_word)
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.end_of_word  # if this is True then only it's a word : return True

    def startsWith(
        self, prefix: str
    ) -> bool:  # do not determine if it's a word : app returns True (apple)
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                if char not in curr.children:
                    return False
            curr = curr.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
