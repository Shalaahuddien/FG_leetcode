class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def bt(path, visited, res):
            # Don't put outer augment in param list if read-only!
            if len(path) == len(nums):
                res.append(list(path))
                return
            for n in nums:
                if n not in visited:
                    visited.add(n)
                    bt(path+[n], visited, res)
                    visited.remove(n)

        res = []
        bt([], set(), res)
        return res