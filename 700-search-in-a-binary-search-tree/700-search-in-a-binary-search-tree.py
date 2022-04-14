# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(T: TreeNode):
            if T:
                if T.val == val:
                    return T
                elif T.val > val:
                    return dfs(T.left)
                else:
                    return dfs(T.right)

        return dfs(root)