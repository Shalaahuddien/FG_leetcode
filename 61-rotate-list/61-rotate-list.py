# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        
        # close to ring, get len
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n+=1
        old_tail.next = head
        
        k %= n
        # all in base-0
        # find new tail n-k-1
        # find new head n -k
        new_tail = head
        for _ in range(n-k-1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        
        # break ring
        new_tail.next = None
        return new_head
        