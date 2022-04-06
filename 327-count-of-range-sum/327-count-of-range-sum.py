class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        presum = [0]
        for n in nums:
            presum.append(presum[-1] + n)
            
        def msort(l,r):
            if l == r:
                return 0
            mid = (l+r)//2
            cnt = msort(l,mid) + msort(mid+1, r)
            i = j = mid+1
            for left in presum[l:mid+1]:
                while i <= r and presum[i] - left < lower:
                    i += 1
                while j <= r and presum[j] - left <= upper:
                    j += 1
                cnt += j-i
            presum[l:r+1] = sorted(presum[l:r+1])
            return cnt
        
        return msort(0, len(presum)-1)