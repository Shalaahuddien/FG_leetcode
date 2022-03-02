# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        if not root:
            return res
        q = [root]
        even = True
        while q:
            nxt = []
            res.append([])
            for n in q:
                res[-1].append(n.val)
                for kid in (n.left, n.right):
                    if kid:
                        nxt.append(kid)
            if not even:
                res[-1].reverse()
            even = not even
            q = nxt
        return res
