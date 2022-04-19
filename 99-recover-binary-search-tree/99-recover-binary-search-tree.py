# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def ino(T: TreeNode) -> bool:
            if not T:
                return False
            nonlocal x, y, pre
            if ino(T.left):
                return True
            if pre and pre.val > T.val:
                y = T
                if not x:
                    x = pre
                else:
                    # BUG: y = T
                    return True
            pre = T
            if ino(T.right):
                return True
        x = y = pre = None
        ino(root)
        x.val, y.val = y.val, x.val