# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        p,s,f = dummy,head, head
        while f and f.next:
          p = p.next
          s,f = s.next, f.next.next
        p.next = p.next.next
        return dummy.next
        