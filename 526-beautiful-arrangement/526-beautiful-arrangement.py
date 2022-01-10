class Solution:
    def countArrangement(self, n: int) -> int:
        sn = set(range(1, n + 1))

        def bt(idx, used, path, res):
            if idx == n + 1:
                res.append(path[:])
                return
            for i in sn - used:
                if not (i % idx == 0 or idx % i == 0):
                    continue
                used.add(i)
                bt(idx + 1, used, path + [i], res)
                used.discard(i)

        res = []
        bt(1, set(), [], res)
        return len(res)