# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        mx = 0

        def post(node: TreeNode, fa):
            if not node:
                return 0
            l,r = post(node.left, node.val), post(node.right, node.val)
            nonlocal mx
            mx = max(mx, l+r)
            return 1 + max(l,r) if node.val == fa else 0
        post(root, None)
        return mx