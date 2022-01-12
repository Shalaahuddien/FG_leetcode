# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(r, v):
            if not r:
                return TreeNode(v)
            if r.val < v:
                r.right = dfs(r.right, v)
            else:
                r.left = dfs(r.left, v)
            return r
        return dfs(root, val)