class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def feasible(thredshold)->bool:
            # check if split m groups, largest sum <= mxs
            count, subsum = 1, 0
            for n in nums:
                subsum += n
                if subsum > thredshold:
                    subsum = n
                    count += 1
                    if count > m:
                        return False
            return True
        
        if m > len(nums): return False
        l,r = max(nums), sum(nums)
        while l < r:
            mid = (l+r)//2
            if feasible(mid):
                r = mid
            else:
                l = mid + 1
        return l