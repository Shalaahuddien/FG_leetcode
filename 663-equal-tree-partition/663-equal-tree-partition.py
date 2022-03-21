# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        node2sum = {}

        def dfs(cur):
            if not cur:
                return 0
            l, r = dfs(cur.left), dfs(cur.right)
            cursum = cur.val + l + r
            node2sum[cur] = cursum
            return cursum

        tot = dfs(root)
        if tot % 2 == 1:
            return False
        for k, v in node2sum.items():
            if k != root and v == tot // 2:
                return True
        return False