# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, target):
            if not node:
                return []
            if not node.left and not node.right:
                if target == node.val:
                    return [[node.val]]
                else:
                    return []
            a = dfs(node.left, target - node.val) + dfs(node.right, target - node.val)
            return [[node.val] + i for i in a]

        return dfs(root, targetSum)