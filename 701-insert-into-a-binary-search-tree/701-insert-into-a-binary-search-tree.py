# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node, v):
            if v < node.val:
                if node.left:
                    dfs(node.left, val)
                else:
                    node.left = TreeNode(val)
                    return
            else:
                if node.right:
                    dfs(node.right, val)
                else:
                    node.right = TreeNode(val)
                    return
        if not root:
            return TreeNode(val)
        dfs(root, val)
        return root