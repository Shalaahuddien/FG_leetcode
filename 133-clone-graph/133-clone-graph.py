"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(u: Node) -> Node:
            """[summary]
            Your runtime beats 66.14 % of python3 submissions.
            """

            if not u:
                return u
            if u in mp:
                return mp[u]
            mp[u] = Node(u.val)
            for v in u.neighbors:
                mp[u].neighbors.append(dfs(v))
            return mp[u]

        mp = {}
        return dfs(node)