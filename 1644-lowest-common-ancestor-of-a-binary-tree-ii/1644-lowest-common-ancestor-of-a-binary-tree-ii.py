# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(node,p,q):
          if not node:
            return None
          if node == p or node == q:
            return node
          l,r = lca(node.left,p,q), lca(node.right,p,q)
          
          if l and r:
            return node
          return l or r
        

        res = lca(root,p,q)
        if res == p:
          pq = lca(p, q,q)
          return res if pq else None
        elif res == q:
          qp = lca(q,p,p)
          return res if qp else None
        return res