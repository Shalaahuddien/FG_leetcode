# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        cnt = 0

        def post(r: TreeNode) -> int:
            if not r:
                return 0
            nonlocal cnt
            subsum = post(r.left) + post(r.right)
            cnt += (subsum == r.val)
            return subsum + r.val

        post(root)
        return cnt
