# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node:
                return []
            if (not node.left) ^ (not node.right):
                r = node.left or node.right
                return [r.val] + dfs(r)
            return dfs(node.left) + dfs(node.right)

        return dfs(root)