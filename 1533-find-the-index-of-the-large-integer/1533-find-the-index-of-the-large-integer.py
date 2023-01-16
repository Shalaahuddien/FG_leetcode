# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        n = reader.length()
        l, r = 0, n - 1

        while l < r:
            mid = (l + r) // 2
            if (r - l + 1) % 2 == 0:
                cmp = reader.compareSub(l, mid, mid + 1, r)
            else:
                cmp = reader.compareSub(l, mid, mid, r)

            if cmp >= 0:
                r = mid
            else:
                l = mid + 1

        return l