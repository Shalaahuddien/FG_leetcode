# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def dfs(T: TreeNode) -> TreeNode:
            if not T:
                return T
            if T.val > high:
                return dfs(T.left)
            elif T.val < low:
                return dfs(T.right)
            else:
                T.left = dfs(T.left)
                T.right = dfs(T.right)
                return T

        return dfs(root)