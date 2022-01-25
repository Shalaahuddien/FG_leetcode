class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(K):
            res, l,r = 0,0,0
            cnt = Counter()
            k = 0
            while r < len(nums):
                c = nums[r]
                if cnt[c] == 0: k += 1
                cnt[c] += 1
                r += 1
                while k > K:
                    d = nums[l]
                    cnt[d] -= 1
                    if cnt[d] == 0: k -= 1
                    l += 1
                res += r-l+1
            return res
        return atMost(k) - atMost(k-1)