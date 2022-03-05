class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
          return 0
        r = max(nums)
        Encode = [0] * (r+1)
        for v in nums:
          Encode[v] += v
        
        def rob(vals):
          F = [0] * len(vals)
          for i in range(len(vals)):
            F[i] = max(
              (F[i-2] if i >= 2 else 0) + vals[i],
              (F[i-1] if i >= 1 else 0)
            )
          return F[-1]
      
        return rob(Encode)
            
          