# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(r):
            if not r:
                return None
            left,right = r.left, r.right
            r.left = dfs(right)
            r.right = dfs(left)
            return r
        return dfs(root)
                