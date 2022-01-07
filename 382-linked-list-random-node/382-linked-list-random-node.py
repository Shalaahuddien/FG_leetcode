# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode) -> None:
        self.h = head

    def getRandom(self) -> int:
        cur = self.h
        cnt = 0
        x = -1

        while cur:
            cnt += 1
            if random.random() < 1 / cnt:
                x = cur.val
            cur = cur.next
        return x



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()