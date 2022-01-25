class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        runsum, ans = 0,0
        sumdict = {0:1}
        for n in nums:
            runsum += n % 2
            if runsum - k in sumdict:
                ans += sumdict[runsum-k]
            sumdict[runsum] = sumdict.get(runsum, 0) + 1
        return ans