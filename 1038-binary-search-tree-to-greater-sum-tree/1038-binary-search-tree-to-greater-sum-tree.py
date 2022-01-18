# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # val = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        def ino(r: TreeNode, sumTillNow):
            if not r:
                return sumTillNow
            sr = ino(r.right, sumTillNow)
            r.val += sr
            return ino(r.left, r.val)

        ino(root, 0)
        return root