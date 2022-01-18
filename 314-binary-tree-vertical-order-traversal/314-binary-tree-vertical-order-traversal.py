# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # (col, node)
        q = deque([(0, root)])
        row = 0
        pos = defaultdict(list)
        mnc, mxc = 0, 0
        while q:
            for _ in range(len(q)):
                col, nod = q.popleft()
                mnc, mxc = min(col, mnc), max(col, mxc)
                pos[col].append(nod.val)
                if nod.left:
                    q.append((col - 1, nod.left))
                if nod.right:
                    q.append((col + 1, nod.right))

            # row += 1
        ans = []
        for c in range(mnc, mxc + 1):
            ans.append(pos[c])
        return ans