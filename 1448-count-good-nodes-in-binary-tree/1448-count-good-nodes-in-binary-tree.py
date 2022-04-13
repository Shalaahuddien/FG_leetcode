# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def post_dfs(T: TreeNode, mx):
            if not T:
                return 0
            res = 1 if T.val >= mx else 0
            mx = max(mx, T.val)
            l, r = post_dfs(T.left, mx), post_dfs(T.right, mx)
            return res + l + r

        return post_dfs(root, -10000)