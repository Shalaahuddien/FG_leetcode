# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def dfs(r: TreeNode, path):
            if r:
                path += str(r.val)
                if not (r.left or r.right):
                    res.append(path)
                    # return
                else:
                    path += "->"
                    dfs(r.left, path)
                    dfs(r.right, path)

        res = []
        dfs(root, "")
        return res