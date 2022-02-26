# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        mn = 2e9
        pre = None

        def ino(r: TreeNode):
            if r.left:
                ino(r.left)
            nonlocal pre, mn
            if pre is not None:
                mn = min(mn, r.val - pre)
            pre = r.val
            if r.right:
                ino(r.right)

        ino(root)
        return mn