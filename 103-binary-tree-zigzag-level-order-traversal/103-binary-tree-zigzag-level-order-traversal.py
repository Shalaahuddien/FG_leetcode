# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        res = []

        def dfs(r: TreeNode, level: int):
            if level >= len(res):
                res.append(deque([r.val]))
            else:
                if level % 2 == 0:
                    res[level].append(r.val)
                else:
                    res[level].appendleft(r.val)

            for kid in [r.left, r.right]:
                if kid:
                    dfs(kid, level + 1)

        dfs(root, 0)
        return res