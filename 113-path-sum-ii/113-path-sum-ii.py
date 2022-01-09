# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, target, path, res):
            # print(node, target, path)
            # if not node:
            #     if target == 0:
            #         return [path]
            #     return [[]]
            if not node:
                return
            if not node.left and not node.right:
                if node.val == target:
                    res.append(path + [node.val])
                    return
            target -= node.val
            dfs(node.left, target, path + [node.val], res)
            dfs(node.right, target, path + [node.val], res)

        res = []
        dfs(root, targetSum, [], res)
        return res