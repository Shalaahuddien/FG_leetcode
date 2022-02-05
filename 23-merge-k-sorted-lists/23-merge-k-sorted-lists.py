# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = h = ListNode(None)
        q = []
        for n in lists:
            if n:
                heappush(q, (n.val, id(n), n))
        while q:
            v, _, n = heappop(q)
            h.next = n
            h = h.next

            if n.next:
                heappush(q, (n.next.val, id(n.next), n.next))
        return dummy.next