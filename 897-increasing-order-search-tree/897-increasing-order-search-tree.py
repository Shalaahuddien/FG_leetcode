# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def dfs(cur: TreeNode):
            l1, r2 = cur, cur
            if cur.left:
                l1, l2 = dfs(cur.left)
                l2.right = cur
            if cur.right:
                r1, r2 = dfs(cur.right)
                cur.right = r1
            cur.left = None
            return (l1, r2)

        return dfs(root)[0]