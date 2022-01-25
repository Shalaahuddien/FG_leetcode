# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        seen = set()

        def dfs(r: TreeNode):
            if not r or (r.right and r.right in seen):
                return None
            seen.add(r)
            r.right = dfs(r.right)
            r.left = dfs(r.left)
            return r

        return dfs(root)