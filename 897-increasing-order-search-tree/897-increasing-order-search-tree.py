# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def dfs(r, tail=None):
            if not r:
                return tail
            res = dfs(r.left, r)
            r.left = None
            r.right = dfs(r.right, tail)
            return res
        return dfs(root)