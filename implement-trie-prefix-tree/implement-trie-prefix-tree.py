class Node:
    def __init__(self) -> None:
        self.isword = False
        self.children = defaultdict(Node)


class Trie:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        p = self.root
        for c in word:
            p = p.children[c]
        p.isword = True
                  
    def search(self, word: str) -> bool:
        p = self.root
        for c in word:
            if c not in p.children:
                return False
            p = p.children[c]
        return p.isword

    def startsWith(self, prefix: str) -> bool:
        p = self.root
        for c in prefix:
            if c not in p.children:
                return False
            p = p.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)