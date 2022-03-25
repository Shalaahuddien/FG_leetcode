# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        f = Counter()

        def ino(T: TreeNode):
            if not T:
                return
            ino(T.left)
            f[T.val] += 1
            ino(T.right)

        ino(root)
        mxf = max(f.values())
        res = []
        for k, v in f.items():
            if v == mxf:
                res.append(k)
        return res
