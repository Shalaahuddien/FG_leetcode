class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def bt(start, path, res):
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                bt(i + 1, path, res)
                path.pop()

        res = []
        bt(0, [], res)
        return res