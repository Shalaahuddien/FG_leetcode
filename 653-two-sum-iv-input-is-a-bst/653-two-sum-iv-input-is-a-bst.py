# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def inorder_itr(r):
            if r:
                yield from inorder_itr(r.left)
                yield r.val
                yield from inorder_itr(r.right)

        def rev_inorder_itr(r):
            if r:
                yield from rev_inorder_itr(r.right)
                yield r.val
                yield from rev_inorder_itr(r.left)

        left_itr, right_itr = inorder_itr(root), rev_inorder_itr(root)
        vi, vj = next(left_itr), next(right_itr)
        while vi < vj:
            if vi + vj == k:
                return True
            elif vi + vj < k:
                vi = next(left_itr)
            else:
                vj = next(right_itr)
        return False
