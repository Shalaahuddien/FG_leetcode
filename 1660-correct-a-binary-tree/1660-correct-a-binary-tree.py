# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        q = deque([(root, None)])
        seen = set()
        while q:
            for _ in range(len(q)):
                r, par = q.popleft()
                seen.add(r)
                if r.right:
                    if r.right in seen:
                        if par.left == r:
                            par.left = None
                        else:
                            par.right = None
                    else:
                        q.append((r.right, r))
                if r.left:
                    q.append((r.left, r))
        return root