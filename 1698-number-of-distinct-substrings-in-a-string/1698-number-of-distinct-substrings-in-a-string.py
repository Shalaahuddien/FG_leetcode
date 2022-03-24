class Solution:
    def countDistinct(self, s: str) -> int:
        class Node:
            def __init__(self) -> None:
                self.child = defaultdict(Node)

        root = Node()
        res = 0
        for i in range(len(s)):
            cur = root
            for j in range(i, len(s)):
                if s[j] not in cur.child:
                    cur.child[s[j]] = Node()
                    res += 1
                cur = cur.child[s[j]]
        return res