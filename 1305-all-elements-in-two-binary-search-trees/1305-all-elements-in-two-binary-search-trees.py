# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def it(r: TreeNode):
            if r:
                yield from it(r.left)
                yield r.val
                yield from it(r.right)

        gen1, gen2 = it(root1), it(root2)

        return list(heapq.merge(gen1, gen2))