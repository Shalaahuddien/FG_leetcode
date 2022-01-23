# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def pre(r, v):
            if r:
                nonlocal total
                v = v<<1 | r.val
                if not r.left and not r.right:
                    total += v
                pre(r.left, v)
                pre(r.right, v)
        
        total = 0
        pre(root, 0)
        return total