# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        AL = defaultdict(list)

        def dfs(par: TreeNode, kid: TreeNode):
            if par and kid:
                AL[par.val].append(kid.val)
                AL[kid.val].append(par.val)
            if kid.left: dfs(kid, kid.left)
            if kid.right: dfs(kid, kid.right)

        dfs(None, root)

        # start BFS from target to all steps == k
        q = deque([target.val])
        seen = set([target.val])
        step = 0
        res = []
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if step == k:
                    res.append(cur)
                    continue
                for neig in AL[cur]:
                    if neig not in seen:
                        seen.add(neig)
                        q.append(neig)
            step += 1
        return res