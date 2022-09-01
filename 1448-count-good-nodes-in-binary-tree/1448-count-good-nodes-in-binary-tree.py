# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def count(node: TreeNode, v: int) -> int:
            if node is None:
                return 0
            mx = max(node.val, v)
            return (node.val >= v) + count(node.left, mx) + count(node.right, mx)
        
        return count(root, root.val)