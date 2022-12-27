class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        count = sorted(c - r for c,r in zip(capacity, rocks))[::-1]
        x = additionalRocks
        while count and x and count[-1] <= x:
            x -= count.pop()
        return len(rocks) - len(count)