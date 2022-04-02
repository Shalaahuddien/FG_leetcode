# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def l2n(l):
            n = 0
            while l:
                n = n * 10 + l.val
                l = l.next
            return n

        def n2l(n):
            dummy = end = ListNode(None)
            for v in str(n):
                end.next = end = ListNode(v)
            return dummy.next

        return n2l(sum(map(l2n, [l1, l2])))
