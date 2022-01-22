# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        q = deque([root])
        has = False
        while q:
            qlen = len(q)
            for i in range(qlen):
                cur = q.popleft()
                if has:
                    return cur
                if cur == u:
                    if i == qlen - 1:
                        return None
                    else:
                        has = True
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return None
