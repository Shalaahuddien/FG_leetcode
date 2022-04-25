# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """
class PeekingIterator:
    def __init__(self, iterator):
        self._iterator = iterator
        self._current = None
        self._hasNext = True
        self.next()

    def peek(self):
        return self._current

    def next(self):
        current = self._current
        if self._iterator.hasNext():
            self._current = self._iterator.next()
        else:
            self._hasNext = False
            
        return current

    def hasNext(self):
        return self._hasNext

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].