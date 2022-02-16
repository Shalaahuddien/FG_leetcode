# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = pre = ListNode(None, head)
        cur = head
        
        while cur and cur.next:
            nxtpair = cur.next.next
            sec = cur.next
            
            # swap
            sec.next = cur
            cur.next = nxtpair
            pre.next = sec
            
            # forward pointers
            pre = cur
            cur = nxtpair
        return dummy.next