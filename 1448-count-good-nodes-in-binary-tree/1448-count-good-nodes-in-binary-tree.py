# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goods = []

        def dfs(node: TreeNode, premax: int):
            if not node:
                return
            if premax <= node.val:
                goods.append(node.val)
            for k in (node.left, node.right):
                dfs(k, max(premax, node.val))

        dfs(root, float('-inf'))
        return len(goods)
