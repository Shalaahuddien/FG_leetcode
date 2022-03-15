# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(r: TreeNode):
            if not r:
                return 0
            return 1 + max(height(r.left), height(r.right))
        
        def dfs(r: TreeNode):
            if not r:
                return True, 0
            bl,hl = dfs(r.left)
            if not bl:
                return False, 0
            br,hr = dfs(r.right)
            if not br:
                return False, 0
            return abs(hl-hr)<=1, 1+max(hl,hr)
        return dfs(root)[0]
            
            