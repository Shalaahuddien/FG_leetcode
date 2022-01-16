# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(r):
            if not r:
                return False
            if k - r.val in seen:
                return True
            seen.add(r.val)

            return dfs(r.left) or dfs(r.right)

        seen = set()
        return dfs(root)