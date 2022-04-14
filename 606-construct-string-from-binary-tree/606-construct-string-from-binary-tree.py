# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        sb = []

        def pre(T: TreeNode):
            nonlocal sb
            sb.append("(")
            if T:
                sb.append(str(T.val))
                if T.left:
                    pre(T.left)
                elif T.right:
                    sb.append("()")
                if T.right:
                    pre(T.right)
            sb.append(")")

        pre(root)
        return ''.join(sb[1:-1])
