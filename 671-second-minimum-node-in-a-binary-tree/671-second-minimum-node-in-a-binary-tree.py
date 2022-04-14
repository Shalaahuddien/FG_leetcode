# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        ans = [float("inf")]
        min1 = root.val

        def dfs(T: TreeNode):
            if T:
                if min1 < T.val < ans[0]:
                    ans[0] = T.val
                elif T.val == min1:
                    dfs(T.left)
                    dfs(T.right)

        dfs(root)
        return ans[0] if ans[0] < float("inf") else -1
