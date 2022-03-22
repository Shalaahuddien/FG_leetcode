# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(T):
            if not T:
                return 0, float('inf'), float('-inf')
            l_n, l_mn, l_mx = dfs(T.left)
            r_n, r_mn, r_mx = dfs(T.right)
            if l_mx < T.val < r_mn:
                return 1+l_n+r_n, min(l_mn, T.val), max(r_mx, T.val)
            return max(l_n,r_n), float('-inf'), float('inf')
        return dfs(root)[0]