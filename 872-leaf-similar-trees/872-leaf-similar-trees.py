# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(T: TreeNode):
            if not T:
                return
            if not (T.left or T.right):
                yield T.val
            for i in dfs(T.left):
                yield i
            for i in dfs(T.right):
                yield i

        return all(a == b for a, b in itertools.zip_longest(dfs(root1), dfs(root2)))