# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def longest_path(root):
            if not root:
                return 0
            length = 1
            l = longest_path(root.left)
            r = longest_path(root.right)
            if root.left and root.left.val == root.val + 1:
                length = max(length, 1 + l)
            if root.right and root.right.val == root.val + 1:
                length = max(length, 1 + r)
            res[0] = max(res[0], length)
            return length
        
        res = [0]
        longest_path(root)
        return res[0]