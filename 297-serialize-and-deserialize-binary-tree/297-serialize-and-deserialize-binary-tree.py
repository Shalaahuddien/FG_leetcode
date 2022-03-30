# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        if not root:
            return "x"
        else:
            return ",".join([str(root.val), self.serialize(root.left), self.serialize(root.right)])

    def deserialize(self, data):
        def dfs():
            v = next(it)
            if v == "x":
                return None
            root = TreeNode(int(v))
            root.left = dfs()
            root.right = dfs()
            return root

        it = iter(data.split(","))
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))