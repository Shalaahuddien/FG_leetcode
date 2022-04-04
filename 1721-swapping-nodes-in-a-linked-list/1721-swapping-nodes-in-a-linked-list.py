# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n1, n2, p = None, None, head
        while p is not None:
            k -= 1
            if n2:
                n2 = n2.next
            if k == 0:
                n1 = p
                n2 = head
            p = p.next
        n1.val, n2.val = n2.val, n1.val
        return head