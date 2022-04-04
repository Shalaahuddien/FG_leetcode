# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(None, head)
        pre, cur = dummy, head
        while cur:
            if cur.next and cur.val == cur.next.val:
                val_to_rm = cur.val
                while cur and cur.val == val_to_rm:
                    cur = cur.next
                # not cur or cur is start non-dup sublist
                pre.next = cur
            else:
                pre, cur = cur, cur.next
        return dummy.next