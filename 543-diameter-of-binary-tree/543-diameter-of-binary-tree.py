# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diam = 0
        def h(r: TreeNode):
            if not r:
                return 0
            lh,rh = map(h, [r.left, r.right])
            nonlocal diam
            diam = max(diam, lh+rh)
            return max(lh,rh)+1
        h(root)
        return diam