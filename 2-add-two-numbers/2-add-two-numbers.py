# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head = ListNode(None)
        c = 0
        while l1 or l2:
            tot = l1.val + l2.val if l1 and l2 else (l1 or l2).val
            c,n = divmod(tot+c, 10)
            head.next = ListNode(n)
            head = head.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if c:
            head.next = ListNode(c)
        return dummy.next
            
            