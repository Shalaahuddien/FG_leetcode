# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        def getLinkedListSize(head):
            size=0
            while head:
                size+=1
                head=head.getNext()
            return size
        
        def helper(head,n):
            if n>1:
                half=head
                for _ in range(n//2):
                    half=half.getNext()
                helper(half,n-n//2)
                helper(head,n//2)
            elif n == 1:
                head.printValue()

        size=getLinkedListSize(head)
        helper(head,size)