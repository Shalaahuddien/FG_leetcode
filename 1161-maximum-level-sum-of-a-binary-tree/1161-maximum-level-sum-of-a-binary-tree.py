# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        mx = -1e9
        ans =lvl = 1
        
        while q:
            qlen = len(q)
            res = 0
            for _ in range(qlen):
                cur = q.popleft()
                res += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            # print(res, lvl)
            if res > mx:
                mx = res
                ans = lvl
            lvl += 1
        return ans