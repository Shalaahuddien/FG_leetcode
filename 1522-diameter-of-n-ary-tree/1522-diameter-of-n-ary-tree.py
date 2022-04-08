"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        self.diam = 0
        def dfs(nod: Node):
            fir = sec = 0
            for k in nod.children:
                dep = dfs(k)
                if dep > fir:
                    fir, sec = dep, fir
                elif dep > sec:
                    sec = dep
            self.diam = max(self.diam, fir + sec)
            return fir + 1

        dfs(root)
        return self.diam