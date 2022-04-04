# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)

        def jump(j) -> ListNode:
            pre, cur = dummy, head
            for i in range(j):
                pre, cur = cur, cur.next
            return cur

        def sz(head):
            l = 0
            while head:
                head = head.next
                l += 1
            return l

        kth = jump(k-1)
        lastkth = jump(sz(head) - k)
        kth.val, lastkth.val = lastkth.val, kth.val
        return dummy.next
