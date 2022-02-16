# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rec(n: ListNode):
            if not n or not n.next:
                return n
            nn = n.next.next
            n, n.next = n.next, n
            n.next.next = rec(nn)
            return n
        return rec(head)