# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stk = []
        self._lefty_inorder(root)
    def _lefty_inorder(self, T):
        while T:
            self.stk.append(T)
            T = T.left
    def next(self) -> int:
        topmost = self.stk.pop()
        if topmost.right:
            self._lefty_inorder(topmost.right)
        return topmost.val

    def hasNext(self) -> bool:
        return len(self.stk) > 0        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()