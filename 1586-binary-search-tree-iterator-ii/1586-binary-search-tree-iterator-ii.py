# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stk = []  # for tree traversal
        self.arr = []  # for storing the vals once it's processed
        self.idx = -1  # ptr for self.list
        # initialize stack with first left inorder
        self._left_ino(root)

    def _left_ino(self, T: TreeNode):
        while T:
            self.stk.append(T)
            T = T.left

    def hasNext(self) -> bool:
        return self.stk or self.idx + 1 < len(self.arr)

    def next(self) -> int:
        self.idx += 1
        if self.idx < len(self.arr):
            return self.arr[self.idx]
        topmost = self.stk.pop()
        self.arr.append(topmost.val)
        # perform left inorder if needed
        self._left_ino(topmost.right)
        return topmost.val

    def hasPrev(self) -> bool:
        return self.idx > 0

    def prev(self) -> int:
        self.idx -= 1
        return self.arr[self.idx]

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.hasNext()
# param_2 = obj.next()
# param_3 = obj.hasPrev()
# param_4 = obj.prev()