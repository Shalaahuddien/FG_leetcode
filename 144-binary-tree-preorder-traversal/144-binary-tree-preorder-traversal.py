# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stk, visited = [], TreeNode(None)
        ret = []

        def pushleftbranch(r: TreeNode):
            while r:
                # preorder
                ret.append(r.val)
                stk.append(r)
                r = r.left

        pushleftbranch(root)
        while stk:
            p = stk[-1]
            # p.left subtree done, but p.right not
            if (not p.left or p.left == visited) and p.right != visited:
                # inorder
                pushleftbranch(p.right)
            # p.right subtree done
            if not p.right or p.right == visited:
                # postorder
                visited = stk.pop()

        return ret