# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaves(T: TreeNode):
            if not T:
                return []
            if not (T.left or T.right):
                return [T.val]
            return leaves(T.left) + leaves(T.right)
        l1, l2 = leaves(root1), leaves(root2)
        return l1 == l2
