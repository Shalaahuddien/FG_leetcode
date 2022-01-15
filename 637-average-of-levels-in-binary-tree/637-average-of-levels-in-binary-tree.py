# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
            dic = defaultdict(list)

            def inorder(r: TreeNode, level):
                if r:
                    inorder(r.left, level + 1)
                    dic[level].append(r.val)
                    inorder(r.right, level + 1)

            inorder(root, 0)

            res = []
            for l in range(len(dic)):
                res.append(sum(dic[l]) / len(dic[l]))
            return res