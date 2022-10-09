# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def get(node, dr):
            if not node: return
            first, last = (node.left, node.right)[::dr]
            yield from get(first, dr)
            yield node.val
            yield from get(last, dr)
        
        head, tail = get(root, 1), get(root, -1)
        n1, n2 = next(head), next(tail)
        while n1 < n2:
            if n1 + n2 < k: n1 = next(head)
            elif n1 + n2 > k: n2 = next(tail)
            else: return True