# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def height(node, heights):
            if not node:
                return -1
            l = height(node.left, heights)
            r = height(node.right, heights)
            lev = max(l, r) + 1
            heights[lev].append(node.val)
            return lev

        dic = defaultdict(list)
        height(root, dic)

        res = []
        for h in range(len(dic)):
            res.append(dic[h])
        return res
