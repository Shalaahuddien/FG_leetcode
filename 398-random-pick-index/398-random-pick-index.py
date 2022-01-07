class Solution:

    def __init__(self, nums: List[int]):
      self.nums = nums
        

    def pick(self, target: int) -> int:
      cnt = 0
      x = -1
      for i,n in enumerate(self.nums):
        if n == target:
          cnt += 1
          if random.random() < 1/cnt:
            x = i
      return x


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)