# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        fas = {}

        def find_fa(node, fa=None):
            if node:
                fas[node] = fa
                find_fa(node.left, node)
                find_fa(node.right, node)

        res = []

        def walk(node, prev, k):
            if not node:
                return
            if k == 0:
                res.append(node.val)
                return
            for v in (node.left, node.right, fas.get(node)):
                if v != prev:
                    walk(v, node, k - 1)
        find_fa(root)
        walk(target, None, k)
        return res