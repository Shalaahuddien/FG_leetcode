# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(r: TreeNode, prefix: int) -> int:
            if r:
                prefix = prefix * 10 + r.val
                if not r.left and not r.right:
                    return prefix

                return dfs(r.left, prefix) + dfs(r.right, prefix)
            else:
                return 0
        return dfs(root, 0)