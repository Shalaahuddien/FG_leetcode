# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stk, visited = [], TreeNode(None)

        def pushleftbranch(r: TreeNode):
            while r:
                # preorder
                r.left, r.right = r.right, r.left

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
                
        return root