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
        lo, hi = 0, n - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if (hi - lo + 1) % 2 == 0:
                compare = reader.compareSub(lo, mid, mid + 1, hi)
            else:
                compare = reader.compareSub(lo, mid, mid, hi)

            # if compare < 0:
            #     lo = mid + 1
            # else:
            #     hi = mid
            if compare >= 0:
                hi = mid
            else:
                lo = mid + 1

        return lo