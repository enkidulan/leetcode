class Node:
    def __init__(self):
        self.word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for i in word:
            node = node.children.setdefault(i, Node())
        node.word=True

    def search(self, word: str) -> bool:
        node = self.root
        for i in word:
            if i not in node.children:
                return False
            node = node.children[i]
        return node.word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in prefix:
            if i not in node.children:
                return False
            node = node.children[i]
        return True




# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
