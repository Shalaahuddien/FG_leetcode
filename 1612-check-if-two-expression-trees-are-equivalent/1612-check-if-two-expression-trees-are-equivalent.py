# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        def dfs(r):
            if not r:
                return []
            # extend(l,r): no return, it only in-place l = l+r
            if r.val == "+":
                return dfs(r.left) + dfs(r.right)
            return [r.val]

        r1 = dfs(root1)
        r2 = dfs(root2)
        return Counter(r1) == Counter(r2)