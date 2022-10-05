# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        v,d = val, depth
        def dfs(node, h, dr):
            if h == d:
                tmp = TreeNode(v)
                #if not node: return tmp
                if dr == 0:
                    tmp.left = node
                else:
                    tmp.right = node
                return tmp
            
            if not node: return node
            
            node.left = dfs(node.left, h+1, 0)
            node.right = dfs(node.right, h+1, 1)
            return node
            
        return dfs(root, 1, 0)