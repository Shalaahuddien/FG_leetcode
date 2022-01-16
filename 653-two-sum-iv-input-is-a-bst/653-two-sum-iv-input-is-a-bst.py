# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def inorder(r):
            if r:
                inorder(r.left)
                ino.append(r.val)
                inorder(r.right)

        ino = []
        inorder(root)
        i, j = 0, len(ino) - 1
        while i < j:
            if ino[i] + ino[j] == k:
                return True
            if ino[i] + ino[j] < k:
                i += 1
            else:
                j -= 1
        return False
