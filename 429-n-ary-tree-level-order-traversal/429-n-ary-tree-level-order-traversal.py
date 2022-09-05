"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root:
          return res
        q = collections.deque([root])
        while q:
          qlen = len(q)
          level = []
          for _ in range(qlen):
            cur = q.popleft()
            level.append(cur.val)
            q.extend(cur.children)
          res.append(level)
        return res