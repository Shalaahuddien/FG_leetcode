# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(r: TreeNode) -> TreeNode:
            """
            Runtime: 20 ms, faster than 99.56% of Python3 online submissions for Invert Binary Tree.

            AC in 1.
            """
            if r:
                r.left, r.right = dfs(r.right), dfs(r.left)
                return r
        return dfs(root)