class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = -1
        for i, n in enumerate(nums):
            if n != 1:
                continue
            if prev != -1:
                if i - prev - 1 < k:
                    return False
            prev = i
        return True