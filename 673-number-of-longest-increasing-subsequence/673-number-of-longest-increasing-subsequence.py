class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        lenLIS, res = 0, 0

        @cache
        def dfs(i):
            mxlen, mxcnt = 1, 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    length, count = dfs(j)
                    if length + 1 > mxlen:
                        mxlen, mxcnt = length + 1, count
                    elif length + 1 == mxlen:
                        mxcnt += count
            nonlocal lenLIS, res
            if mxlen > lenLIS:
                lenLIS, res = mxlen, mxcnt
            elif mxlen == lenLIS:
                res += mxcnt
            return (mxlen, mxcnt)

        for i in range(len(nums)):
            dfs(i)
        return res