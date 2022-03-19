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
        def is_subpath(h, r):
            if not h:
                return True
            if not r:
                return False
            if is_same(h, r):
                return True
            return is_subpath(h, r.left) or is_subpath(h, r.right)

        def is_same(h, r):
            if not h:
                return True
            if not r:
                return False
            if h.val != r.val:
                return False
            return is_same(h.next, r.left) or is_same(h.next, r.right)

        return is_subpath(head, root)