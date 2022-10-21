class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n2lr = {}
        for i, n in enumerate(nums):
            if n in n2lr:
                if i - n2lr[n] <= k:
                    return True
                n2lr[n] = i

            else:
                n2lr[n] = i

        return False