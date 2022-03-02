"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        mp = {}

        def dfs(r: Node) -> Node:
            if not r:
                return None
            if r not in mp:
                mp[r] = Node(r.val)
            for kid in r.children:
                mp[r].children.append(dfs(kid))
            return mp[r]

        return dfs(root)