# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        tmp = {}

        def dfs(T: TreeNode, par: TreeNode, dep):
            if not T:
                return
            if T.val in [x, y]:
                tmp[T.val] = [par, dep]
            dfs(T.left, T, dep + 1)
            dfs(T.right, T, dep + 1)

        dfs(root, None, 0)
        if tmp[x][1] == tmp[y][1] and tmp[x][0] != tmp[y][0]:
            return True
        return False