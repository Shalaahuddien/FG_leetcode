# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        have_none = False
        q = deque([root])
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if not cur:
                    have_none = True
                    continue
                if have_none:
                    return False
                q.append(cur.left)
                q.append(cur.right)
        return True