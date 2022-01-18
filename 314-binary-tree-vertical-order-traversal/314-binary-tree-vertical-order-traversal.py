# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        pos = defaultdict(list)

        def dfs(r, row, col):
            if r:
                dfs(r.left, row + 1, col - 1)
                pos[col].append((row, (r.val)))
                dfs(r.right, row + 1, col + 1)

        dfs(root, 0, 0)

        res = []
        for c in sorted(pos):
            res.append(
                [v for r, v in sorted(pos[c], key=lambda tu: (tu[0]))])
        return res
