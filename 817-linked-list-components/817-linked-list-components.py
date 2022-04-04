# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        cc = len(nums)
        vals = set(nums)
        pre, cur = None, head
        while cur:
            pre, cur = cur, cur.next
            if pre.val in vals and cur and cur.val in vals:
                cc -= 1
        return cc
