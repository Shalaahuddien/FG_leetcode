# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def dfs(T: TreeNode, par: TreeNode, dep, mp: dict):
            if not T or len(mp) == 2:
                return
            if T.val in [x, y]:
                mp[T.val] = [par, dep]
            dfs(T.left, T, dep + 1, mp)
            dfs(T.right, T, dep + 1, mp)

        mp = {}
        dfs(root, None, 0, mp)
        if mp[x][1] == mp[y][1] and mp[x][0] != mp[y][0]:
            return True
        return False