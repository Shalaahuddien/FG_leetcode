# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        @cache
        def dp(h, r):
            if not h:
                return True
            if not r:
                return False
            if h.val == r.val:
                return dp(h.next, r.left) or dp(h.next, r.right) or dp(head, r.left) or dp(head, r.right)
            else:
                return dp(head, r.left) or dp(head, r.right)

        return dp(head, root)