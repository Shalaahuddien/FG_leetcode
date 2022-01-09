# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        def lca(node):
            if not node:
                return None
            if node in nodes:
                return node

            l,r = lca(node.left), lca(node.right)
            if l and r:
                return node
            return l or r

        return lca(root)