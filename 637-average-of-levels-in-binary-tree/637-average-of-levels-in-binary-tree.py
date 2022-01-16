# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        dic = defaultdict(int)
        q = deque([root])
        level = 0
        ans = []
        while q:
            qlen = len(q)
            for _ in range(qlen):
                c = q.popleft()
                dic[level] += c.val
                for k in (c.left, c.right):
                    if k:
                        q.append(k)
            ans.append(dic[level] / qlen)
            level += 1

        return ans