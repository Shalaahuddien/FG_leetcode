# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        mx = 0

        def post(node: TreeNode):
            if not node:
                return 0
            pass_node = 0
            longest = 1
            nonlocal mx
            for kid in (node.left, node.right):
                side = post(kid)
                if kid and kid.val == node.val:
                    pass_node += side
                    longest = max(longest, 1 + side)
            mx = max(mx, pass_node)
            return longest

        post(root)
        return mx