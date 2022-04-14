# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        total = 0
        sms = []

        def dfs(T: TreeNode):
            if not T:
                return 0
            l, r = dfs(T.left), dfs(T.right)
            smT = l + r + T.val
            sms.append(smT)
            return smT

        MOD = 10**9 + 7
        total = dfs(root)
        ans = 0
        for s in sms:
            ans = max(ans, s * (total - s))
        return ans % MOD