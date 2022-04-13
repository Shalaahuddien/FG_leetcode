# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        u2fa = {}

        def dfs(node: TreeNode, fa=None):
            if node:
                u2fa[node] = fa
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root, None)

        q = deque([(target, 0)])
        seen = {target}
        while q:
            u, d = q.popleft()
            if d == k:
                return [u.val] + [n.val for n, d in q]
            for v in (u.left, u.right, u2fa[u]):
                if v and v not in seen:
                    seen.add(v)
                    q.append((v, d + 1))
        return []