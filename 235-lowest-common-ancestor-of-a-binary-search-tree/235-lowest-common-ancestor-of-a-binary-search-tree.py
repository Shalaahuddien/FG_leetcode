# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca_sol(cur: TreeNode)->TreeNode:
            if cur.val > max(p.val, q.val):
                return lca_sol(cur.left)
            elif cur.val < min(p.val, q.val):
                return lca_sol(cur.right)
            return cur


        return lca_sol(root)