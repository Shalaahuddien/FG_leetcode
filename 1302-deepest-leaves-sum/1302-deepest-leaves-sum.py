# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        bfs = deque([root])
        while bfs:
            tmp = 0
            for _ in range(len(bfs)):
                n = bfs.popleft()
                tmp += n.val
                for k in [n.left, n.right]:
                    if k:
                        bfs.append(k)
            if not bfs:
                return tmp