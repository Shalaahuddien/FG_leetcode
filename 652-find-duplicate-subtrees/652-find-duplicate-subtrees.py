# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        dic = {}
        results = []
        def postorder(root):
            
            if root is None:
                return '#'
            subTree = postorder(root.left) + ',' + postorder(root.right) + ',' + str(root.val)
            if subTree in dic.keys():
                dic[subTree] += 1
            else:
                dic[subTree] = 1
            if dic[subTree] == 2:
                results.append(root)
            return subTree

        postorder(root)
        return results