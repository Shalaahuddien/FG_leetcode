class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def feasible(mxs)->bool:
            # check if split m groups, largest sum <= mxs
            count, sm = 1, 0
            for n in nums:
                if sm + n > mxs:
                    count += 1
                    if count > m:
                        return False
                    sm = n
                else:
                    sm += n
            return count <= m
        
        if m > len(nums): return False
        l,r = max(nums), sum(nums)
        while l < r:
            mid = (l+r)//2
            if feasible(mid):
                r = mid
            else:
                l = mid + 1
        return l