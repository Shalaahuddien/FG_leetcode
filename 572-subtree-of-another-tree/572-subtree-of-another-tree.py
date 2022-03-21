# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same(r, s):
            if r and s:
                return r.val == s.val and is_same(r.left, s.left) and is_same(r.right, s.right)
            return r == s

        def dfs(r, s):
            if not r:
                return False
            if is_same(r, s):
                return True
            return dfs(r.left, s) or dfs(r.right, s)

        return dfs(root, subRoot)