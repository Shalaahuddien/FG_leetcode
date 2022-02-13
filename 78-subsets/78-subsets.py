class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def bt(start, path, res):
            res.append(path[:])
            for i in range(start, len(nums)):
                bt(i + 1, path + [nums[i]], res)

        res = []
        bt(0, [], res)
        return res