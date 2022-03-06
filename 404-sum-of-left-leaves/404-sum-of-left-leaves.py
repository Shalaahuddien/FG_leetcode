# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(r, isleft) -> int:
            if not r:
                return 0
            if not (r.left or r.right) and isleft:
                return r.val

            return dfs(r.left, True) + dfs(r.right, False)

        return dfs(root, False)
