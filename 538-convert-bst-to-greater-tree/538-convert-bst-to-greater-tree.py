# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def ino(T: TreeNode, sumTillNow):
            if T:
                ino(T.right, sumTillNow)
                T.val += sumTillNow[0]
                sumTillNow[0] = T.val
                ino(T.left, sumTillNow)

        ino(root, [0])
        return root
