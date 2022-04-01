class Solution:
    def expand(self, s: str) -> List[str]:
        def bt(i, path, res):
            if i == len(q):
                res.append("".join(path))
                return
            if q[i] not in "{}":
                bt(i + 1, path + [q[i]], res)
            if q[i] == "{":
                j = q.index("}", i + 1)
                opt = q[i + 1 : j].split(",")
                opt.sort()

                for c in opt:
                    bt(j + 1, path + [c], res)

        q = s
        res = []
        bt(0, [], res)
        return res