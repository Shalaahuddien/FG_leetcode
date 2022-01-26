# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        stk1, stk2, res = [], [], []
        r1, r2 = root1, root2
        while r1 or r2 or stk1 or stk2:
            # update both stacks
            # by going left till possible
            while r1:
                stk1.append(r1)
                r1 = r1.left
            while r2:
                stk2.append(r2)
                r2 = r2.left

            # Add the smallest value into output,
            # pop it from the stack,
            # and then do one step right
            if not stk2 or (stk1 and stk1[-1].val <= stk2[-1].val):
                r1 = stk1.pop()
                res.append(r1.val)
                r1 = r1.right

            else:
                r2 = stk2.pop()
                res.append(r2.val)
                r2 = r2.right
        return res