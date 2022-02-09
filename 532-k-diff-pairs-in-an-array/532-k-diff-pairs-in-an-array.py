class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        pairs = set()
        nums.sort()
        for i, x in enumerate(nums):
            for y in {x - k, x + k}:
                j = bisect_right(nums, y)
                if j == 0:
                    continue
                if j - 1 <= i:
                    continue
                if nums[j - 1] != y:
                    continue
                pairs.add((x, y))
        return len(pairs)