# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(cur, path, res):
            if not cur:
                return
            if not cur.left and not cur.right:
                v = 0
                for n in path+[cur.val]:
                    v = v * 2 + int(n)
                res.append(v)
                return
            path += [cur.val]
            dfs(cur.left, path, res)
            dfs(cur.right, path, res)
            path.pop()
            return

        res = []
        dfs(root, [], res)
        # print(res)
        return sum(res)