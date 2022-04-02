# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        addends = l1,l2
        dummy = end = ListNode(None)
        carry = 0
        while addends or carry:
            carry += sum(l.val for l in addends)
            addends = [l.next for l in addends if l.next]
            carry,d = divmod(carry, 10)
            end.next = end = ListNode(d)
        return dummy.next