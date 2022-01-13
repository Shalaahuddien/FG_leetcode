# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def inorder(r, level):
            if r:
                inorder(r.left, level + 1)
                level_sum[level] += r.val
                inorder(r.right, level + 1)

        level_sum = defaultdict(int)
        inorder(root, 1)

        # Choose the level with the greatest sum "level_sum[level]" and if
        # there is a tie, then select the smaller level "-level".
        return max(level_sum, key=lambda level: (level_sum[level], -level))
