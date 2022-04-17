# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def ino(T: TreeNode)->None:
            if T:
                ino(T.left)
                T.left = None
                nonlocal end
                end.right = T
                end = T
                ino(T.right)
        dummy = end = TreeNode(None)
        ino(root)
        return dummy.right