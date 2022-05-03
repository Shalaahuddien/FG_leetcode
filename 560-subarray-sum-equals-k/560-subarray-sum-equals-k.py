class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt, cur, res = {0:1}, 0, 0
        for n in nums:
            cur +=n 
            res += cnt.get(cur-k, 0) 
            cnt[cur] = cnt.get(cur, 0)+1
        return res