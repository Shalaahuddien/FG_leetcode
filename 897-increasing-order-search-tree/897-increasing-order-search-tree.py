# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ans = cur = TreeNode(None)

        def ino(r: TreeNode):
            if r:
                ino(r.left)
                r.left = None
                nonlocal cur
                cur.right = r
                cur = r
                ino(r.right)

        ino(root)
        return ans.right
