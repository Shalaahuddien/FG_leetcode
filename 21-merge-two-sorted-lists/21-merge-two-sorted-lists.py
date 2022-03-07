# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def dfs(p, q):
            if not p:
                return q
            elif not q:
                return p
            elif p.val < q.val:
                p.next = dfs(p.next, q)
                return p
            else:
                q.next = dfs(p, q.next)
                return q

        return dfs(l1, l2)