# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def rev(head: ListNode):
            pre, cur = None, head
            while cur:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            return pre

        def pochmann_2(l1, l2):
            addends = l1, l2
            carry = 0
            dummy = end = ListNode(None)
            while addends or carry:
                carry += sum(l.val for l in addends)
                addends = [l.next for l in addends if l.next]
                carry,d = divmod(carry, 10)
                end.next = end = ListNode(d)
            return dummy.next

        return rev(pochmann_2(rev(l1), rev(l2)))