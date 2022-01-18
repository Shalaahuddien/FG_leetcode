# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        pos = defaultdict(list)
        cols = [0, 0]

        def dfs(r, row, col):
            nonlocal cols
            if r:
                cols = [min(col, cols[0]), max(col, cols[1])]
                dfs(r.left, row + 1, col - 1)
                pos[col].append((row, (r.val)))
                dfs(r.right, row + 1, col + 1)

        dfs(root, 0, 0)

        res = []
        for c in range(cols[0], cols[1] + 1):
            res.append(
                [v for r, v in sorted(pos[c], key=lambda tu: (tu[0]))])
            # res.append([v for r, v in pos[c]])
        return res
