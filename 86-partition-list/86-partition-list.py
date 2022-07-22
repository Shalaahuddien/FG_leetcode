# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l = ListNode(None)
        ge = ListNode(None)
        ld,ged = l,ge
        n = head
        while n:
            if n.val < x:
                l.next = n
                l= l.next
            else:
                ge.next = n
                ge = ge.next
            n = n.next
        ge.next = None
        l.next = ged.next
        return ld.next