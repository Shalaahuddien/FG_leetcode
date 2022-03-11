# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(r):
            if r:
                nonlocal ans
                
                if low <= r.val <= high:
                    ans += r.val
                if low < r.val:
                    dfs(r.left)
                if r.val < high:
                    dfs(r.right)
            return ans
        
        ans = 0
        dfs(root)
        return ans