# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def preorder(r, cur_num):
            nonlocal root_to_leaf
            if r:
                cur_num = (cur_num << 1) | r.val
                if not (r.left or r.right):
                    root_to_leaf += cur_num
                preorder(r.left, cur_num)
                preorder(r.right, cur_num)

        root_to_leaf = 0
        preorder(root, 0)
        return root_to_leaf