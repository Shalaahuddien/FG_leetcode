# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, D: List[List[int]]) -> Optional[TreeNode]:
        d = {}  # v -> node
        kid = set()
        for x in D:
            p, c, l = x
            kid.add(c)
            if c not in d:
                d[c] = TreeNode(c)
            if p not in d:
                d[p] = TreeNode(p)
            if l:
                d[p].left = d[c]
            else:
                d[p].right = d[c]
        # print(set(d.keys()))
        # print(kid)
        # print((set(d.keys()) - kid).pop())
        return d[(set(d.keys()) - kid).pop()]