class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns = set(nums)
        best = 0
        for x in ns:
            if x-1 not in ns:
                y=x+1
                while y in ns:
                    y += 1
                best = max(best, y-x)
        return best