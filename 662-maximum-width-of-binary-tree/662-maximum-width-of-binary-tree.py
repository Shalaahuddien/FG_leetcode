# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        if not root:
            return ans
        q = deque([(root, 0)])
        while q:
            next_q = []
            ans = max(ans, q[-1][1] - q[0][1]+1)
            for cur, idx in q:
                if cur.left:
                    next_q.append((cur.left, idx * 2))
                if cur.right:
                    next_q.append((cur.right, idx * 2 + 1))
            q = next_q
        return ans