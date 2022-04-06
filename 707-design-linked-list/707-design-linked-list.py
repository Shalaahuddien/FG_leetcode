class Node:
    def __init__(self, val: int, next=None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return str(self.val)


class MyLinkedList:
    def __init__(self):
        self.dummy = Node(None)
        self.sz = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.sz:
            return -1
        end = self.dummy
        for _ in range(index + 1):
            end = end.next
        return end

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.sz, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.sz:
            return
        prev = self.dummy
        for _ in range(index):
            prev = prev.next

        # add new node between [prev] and [prev.next]
        new = Node(val, prev.next)
        prev.next = new
        self.sz += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.sz:
            return
        prev = self.dummy
        for _ in range(index):
            prev = prev.next
        prev.next = prev.next.next
        self.sz -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)