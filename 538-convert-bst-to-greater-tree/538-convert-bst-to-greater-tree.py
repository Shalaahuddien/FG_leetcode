# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        acc = 0
        def ino(r):
            nonlocal acc

            if r:
                ino(r.right)
                r.val += acc
                acc = r.val
                ino(r.left)
                return r
            
        ino(root)
        return root