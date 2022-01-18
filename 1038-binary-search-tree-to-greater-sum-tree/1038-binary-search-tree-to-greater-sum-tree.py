# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # val = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        pre = 0

        def inord(r: TreeNode):
            nonlocal pre
            if r:
                inord(r.right)
                r.val = pre = pre + r.val
                inord(r.left)
                return r

        return inord(root)