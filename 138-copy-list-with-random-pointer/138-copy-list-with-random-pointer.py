"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = {}

        def dfs(u: Node):
            if not u:
                return None
            if u in d:
                return d[u]
            u2 = Node(u.val, None, None)
            d[u] = u2
            u2.next = dfs(u.next)
            u2.random = dfs(u.random)
            return u2

        return dfs(head)
