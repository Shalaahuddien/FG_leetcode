# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        bfs = deque([root])
        ans = 0
        while bfs:
            ans = 0
            for _ in range(len(bfs)):
                n = bfs.popleft()
                ans += n.val
                for k in [n.left, n.right]:
                    if k:
                        bfs.append(k)
        return ans