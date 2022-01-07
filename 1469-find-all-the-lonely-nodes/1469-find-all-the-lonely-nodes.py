# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, res):
            if not node:
                return
            dfs(node.left, res)
            dfs(node.right, res)
            if not node.left and not node.right:
                return
            if not node.left or not node.right:
                lonely = node.left or node.right
                res.append(lonely.val)
        res = []
        dfs(root, res)
        return res