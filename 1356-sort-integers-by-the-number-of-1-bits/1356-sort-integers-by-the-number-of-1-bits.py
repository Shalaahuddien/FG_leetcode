class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def bits(v):
            ones = 0
            while v:
                ones += 1
                v &= v - 1
            return ones

        arr.sort(key=lambda x: (bits(x), x))
        return arr