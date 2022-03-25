"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root):
        ser = []

        def dfs(T: Node):
            if not T:
                return
            ser.append(str(T.val))
            for k in T.children:
                dfs(k)
            ser.append("!")

        dfs(root)
        return " ".join(ser)

    def deserialize(self, data):
        if not data:
            return None
        tokens = deque(data.split(" "))
        root = Node(int(tokens.popleft()), [])

        def helper(T: Node):
            if not tokens:
                return
            while tokens[0] != "!":
                v = tokens.popleft()
                kid = Node(int(v), [])
                T.children.append(kid)
                helper(kid)
            tokens.popleft()  # discard the '!'

        helper(root)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))