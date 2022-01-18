# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # val = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        def ino(r,acc):
            if r:
                ino(r.right,acc)
                r.val += acc[0]
                acc[0] = r.val
                ino(r.left, acc)
                return r
        ino(root,[0])
        return root