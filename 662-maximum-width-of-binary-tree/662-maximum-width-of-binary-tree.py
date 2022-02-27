# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        first_col_idx_table = {}
        mx_width = 0

        def dfs(node: TreeNode, depth, col_idx):
            if not node:
                return
            if depth not in first_col_idx_table:
                first_col_idx_table[depth] = col_idx
            nonlocal mx_width

            mx_width = max(mx_width, col_idx - first_col_idx_table[depth] + 1)

            dfs(node.left, depth + 1, col_idx * 2)
            dfs(node.right, depth + 1, col_idx * 2 + 1)

        dfs(root, 0, 0)
        return mx_width