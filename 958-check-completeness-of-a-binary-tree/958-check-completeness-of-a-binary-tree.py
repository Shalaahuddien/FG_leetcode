# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        pre = root
        while q:
            # have_none = False # WA: [1,2,3,4,5,6,7,8,9,10,11,12,13,null,null,15]
            for _ in range(len(q)):
                cur = q.popleft()
                if cur:
                    if not pre:
                        return False
                    q.append(cur.left)
                    q.append(cur.right)
                pre = cur
        return True