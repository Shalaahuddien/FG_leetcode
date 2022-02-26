# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        mn = 2e9
        io = []

        def ino(r: TreeNode):
            if not r:
                return None
            ino(r.left)
            io.append(r.val)
            ino(r.right)
            
        ino(root)


        for i in range(1, len(io)):
            mn = min(mn, abs(io[i] - io[i - 1]))
        return mn