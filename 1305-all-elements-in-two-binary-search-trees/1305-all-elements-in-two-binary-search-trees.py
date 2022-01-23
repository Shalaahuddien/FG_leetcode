# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def ino(r: TreeNode, lst: list[int]):
            if r:
                ino(r.left, lst)
                lst.append(r.val)
                ino(r.right, lst)

        li1, li2 = [], []
        ino(root1, li1)
        ino(root2, li2)

        L1, L2 = len(li1), len(li2)
        i, j = 0, 0
        ans = []
        while i < L1 and j < L2:
            if li1[i] < li2[j]:
                ans.append(li1[i])
                i += 1
            else:
                ans.append(li2[j])
                j += 1
        return ans + li1[i:] + li2[j:]