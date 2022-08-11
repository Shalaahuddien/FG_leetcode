# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
      def check(node, mn,mx):
        if not node:
          return True
        if not mn < node.val< mx:
          return False
        return check(node.left, mn, node.val) \
            and check(node.right, node.val, mx)
      
      return check(root, float('-inf'), float('inf'))