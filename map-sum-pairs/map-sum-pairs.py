class Node:
    def __init__(self) -> None:
        self.children = defaultdict(Node)
        self.sum = 0


class MapSum:
    """
    Runtime: 71 ms, faster than 5.13% of Python3 online submissions for Map Sum Pairs.

    T: insert: O(K), sum: O(P)
    # K: len of key string, P: len of prefix string
    """
    def __init__(self):
        self.root = Node()
        self.kv = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        delta = val - self.kv[key]
        self.kv[key] = val
        p = self.root
        for c in key:
            p = p.children[c]
            p.sum += delta

    def sum(self, prefix: str) -> int:
        p = self.root
        for c in prefix:
            p = p.children[c]
        return p.sum

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)