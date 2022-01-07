# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        cur = head
        i = 0
        self.D = {}
        while cur:
            self.D[i] = cur.val
            cur = cur.next
            i += 1
        print(self.D)
        
    def getRandom(self) -> int:
        r = int(random.random()*len(self.D))
        print(r)
        return self.D[r]



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()