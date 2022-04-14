# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(l, r):
            if l == r:
                return TreeNode(nums[l])
            if l > r:
                return None
            mx = -1
            mxi = -1
            for i in range(l, r + 1):
                if nums[i] > mx:
                    mx = nums[i]
                    mxi = i
            subl, subr = dfs(l, mxi - 1), dfs(mxi + 1, r)
            return TreeNode(mx, subl, subr)

        return dfs(0, len(nums) - 1)
