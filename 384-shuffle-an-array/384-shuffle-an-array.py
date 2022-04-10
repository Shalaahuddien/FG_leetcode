class Solution:
    def __init__(self, nums: List[int]):
        self.arr = nums
        self.ori = list(nums)

    def reset(self) -> List[int]:
        self.arr = self.ori
        self.ori = list(self.ori)
        return self.arr

    def shuffle(self) -> List[int]:
        def swap(A, i, j):
            A[i], A[j] = A[j], A[i]

        for i in range(len(self.arr)):
            swap_idx = randrange(i, len(self.arr))
            swap(self.arr, swap_idx, i)
        return self.arr

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()