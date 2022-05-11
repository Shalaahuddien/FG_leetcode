class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def bt(k, n, lower, path, res):
            if k == 0 and n == 0:
                res.append(path[:])
                return
            for v in range(lower + 1, 10):
                bt(k - 1, n - v, v, path + [v], res)

        res = []
        bt(k, n, 0, [], res)
        return res