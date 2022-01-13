# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.ps= deque()
        self.root = root
        q = deque([root])
        
        while q:
            c = q.popleft()
            if not c.left or not c.right:
                self.ps.append(c)
            if c.left:
                q.append(c.left)
            if c.right:
                q.append(c.right)

    def insert(self, val: int) -> int:
        p = self.ps[0]
        self.ps.append(TreeNode(val))
        if not p.left:
            p.left = self.ps[-1]
        else:
            p.right = self.ps[-1]
            self.ps.popleft()
        return p.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()