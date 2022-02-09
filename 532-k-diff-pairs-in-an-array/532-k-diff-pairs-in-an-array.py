class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        cnt = 0
        nums.sort()
        for i, x in enumerate(nums):
            if i != 0 and nums[i - 1] == x:
                continue
            for y in {x - k, x + k}:
                j = bisect_right(nums, y)
                if j == 0:
                    continue
                if j - 1 <= i:
                    continue
                if nums[j - 1] != y:
                    continue
                # pairs.append((x, y))
                cnt += 1
        return cnt