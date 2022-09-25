# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, sm):
            if not node: return []
            if not node.left and not node.right and sm == node.val:
                return [[node.val]]
           
            lft = dfs(node.left, sm - node.val)
            rgh = dfs(node.right, sm - node.val)
            return [cand + [node.val] for cand in lft + rgh]
            
        return [s[::-1] for s in dfs(root, targetSum)]