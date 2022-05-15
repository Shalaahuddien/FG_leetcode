# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def dep(T: TreeNode):
            if not T:
                return 0
            return max(dep(T.left), dep(T.right))+1

        def dfs(T: TreeNode, d: int)->int:
            if not T:
                return 0
            if d == 0:
                return T.val
            else:
                return dfs(T.left, d-1) + dfs(T.right, d-1)

        return dfs(root, dep(root)-1)