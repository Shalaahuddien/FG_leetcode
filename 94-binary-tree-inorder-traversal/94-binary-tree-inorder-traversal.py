# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      res, stk = [], [(root, False)]
      while stk:
        cur, visited = stk.pop()
        if not cur:
          continue
        if visited:
          res.append(cur.val)
        else:
          # inorder: LVR -> RVL
          stk.append((cur.right, False))
          stk.append((cur, True))
          stk.append((cur.left, False))
      return res