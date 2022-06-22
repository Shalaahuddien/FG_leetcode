class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        def lomuto(lo, hi):
            swap(randint(lo, hi), hi)
            l = lo - 1
            for i in range(lo, hi):
                if nums[hi] > nums[i]:
                    l += 1
                    swap(l, i)
            swap(l + 1, hi)
            return l + 1

        kk = len(nums) - k

        def qselect(beg, end):
            if beg >= end:
                return nums[beg]
            pi = lomuto(beg, end)
            if pi == kk:
                return nums[kk]
            elif pi < kk:
                return qselect(pi + 1, end)
            return qselect(beg, pi - 1)

        return qselect(0, len(nums) - 1)