# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def f(node: TreeNode, lo, hi):
            if not node:
                return hi - lo
            l = f(node.left, lo, node.val)
            r = f(node.right, node.val, hi)
            return min(l, r)

        return f(root, -2e9, 2e9)