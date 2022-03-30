"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        ser = []
        def dfs(T: Node):
            if not T:
                return 
            ser.append(str(T.val))
            for k in T.children:
                dfs(k)
            ser.append('!')
        dfs(root)
        return ','.join(ser)
        
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        q = deque(data.split(','))
        def fn():
            if not q:
                return None
            node = Node(int(q.popleft()), [])
            while q[0] != '!':
                node.children.append(fn())
            q.popleft()
            return node
        return fn()
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))