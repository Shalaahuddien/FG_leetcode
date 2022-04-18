# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def dfs(T: TreeNode, next)->TreeNode:
            if not T:
                return next
            head = dfs(T.left, T)
            T.left =None
            T.right = dfs(T.right, next)
            return head
        return dfs(root, None)