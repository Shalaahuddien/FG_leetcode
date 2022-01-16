# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        cnt = defaultdict(int)

        def dfs(r):
            if r:
                cnt[r.val] += 1
                dfs(r.left)
                dfs(r.right)

        dfs(root)
        for v in cnt:
            if k - v in cnt:
                if k == 2 * v:
                    if cnt[v] > 1:
                        return True
                    continue
                return True
        return False