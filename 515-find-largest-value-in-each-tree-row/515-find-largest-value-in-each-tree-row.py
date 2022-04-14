# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        q = deque([root])
        while q:
            mx = float("-inf")
            for _ in range(len(q)):
                cur = q.popleft()
                mx = max(mx, cur.val)
                for k in filter(None, [cur.left, cur.right]):
                    q.append(k)
            res.append(mx)
        return res