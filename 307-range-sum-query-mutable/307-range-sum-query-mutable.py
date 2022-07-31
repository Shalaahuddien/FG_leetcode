class NumArray:

    def __init__(self, nums):
        self.n = len(nums)
        self.a, self.c = nums, [0] * (self.n + 1)
        for i in range(self.n):
            k = i + 1
            while k <= self.n:
                self.c[k] += nums[i]
                k += (k & -k)

    def update(self, i, val):
        diff, self.a[i] = val - self.a[i], val
        i += 1
        while i <= self.n:
            self.c[i] += diff
            i += (i & -i)

    def sumRange(self, i, j):
        res, j = 0, j + 1
        while j:
            res += self.c[j]
            j -= (j & -j)
        while i:
            res -= self.c[i]
            i -= (i & -i)
        return res
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)