# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mergesort(head: Optional[ListNode]) -> Optional[ListNode]:

            def _middle(head: ListNode):
                '''
                Linked-list snippet. Return len//2 node as mid
                XXX: don't forget to unlink prev.
                '''
                pre, s, f = None, head, head
                while f and f.next:
                    pre, s, f = s, s.next, f.next.next
                pre.next = None
                return s

            def _merge(l1: ListNode, l2: ListNode) -> ListNode:
                '''
                linked-list snippet: merge 2 sorted list.
                '''
                ptr = dummy = ListNode(None)
                while l1 and l2:
                    # while both l1&l2, loop invariant: tail points to min(l1,l2)
                    if l1.val < l2.val:
                        ptr.next = l1
                        l1 = l1.next
                    else:
                        ptr.next = l2
                        l2 = l2.next
                    ptr = ptr.next
                ptr.next = l1 or l2
                return dummy.next

            if not head or not head.next:
                return head

            mid = _middle(head)
            sl1 = mergesort(head)
            sl2 = mergesort(mid)
            return _merge(sl1, sl2)

        return mergesort(head)
