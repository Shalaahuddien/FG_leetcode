# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        def dfs_l(T: TreeNode):
            if not T or not T.left and not T.right:
                return
            boundary.append(T.val)
            if T.left:
                dfs_l(T.left)
            else:
                dfs_l(T.right)

        def leaves(T: TreeNode):
            # why
            if not T:
                return
            leaves(T.left)
            if T != root and not T.left and not T.right:
                boundary.append(T.val)
            leaves(T.right)

        def dfs_r(T: TreeNode):
            if not T or not T.left and not T.right:
                return
            if T.right:
                dfs_r(T.right)
            else:
                dfs_r(T.left)
            boundary.append(T.val)

        if not root:
            return []
        boundary = [root.val]
        dfs_l(root.left)
        leaves(root)
        dfs_r(root.right)
        return boundary